# Kafka无丢失无乱序配置


**kafka生产者端：**

1. 配置acks = all或-1，所有follower都响应了才认为消息提交成功
2. 配置retries = MAX_VALUE，重试次数设为最大（并不会无限重试delivery.timeout.ms超时后，如果重试次数没有用尽，传输超时也会停止）
3. 配置max.in.flight.requests.per.connection = 1，限制单个连接上能够发送的未响应请求的个数。设置此值是1表示kafka broker在响应请求之前producer不能再向同一个broker发送请求。设置此参数是为了避免消息乱序
4. 使用KafkaProducer.send(record, callback)自定义回调逻辑处理消息发送失败，失败给出告警
5. callback逻辑中显式关闭producer.close(Duration.ofMillis(0))，不可重试异常，立即关闭，防止默认关闭前发送后面的消息，而发生乱序
6. 保证每个表的数据都能进入同一个partition（通过BKDR hash算法），保证消息有序

**broker端：**

1. unclean.leader.election.enable=false，关闭unclean选举（非同步状态副本），防止broker端因水位截断造成消息丢失
2. replication.factor = 3，大于等于3，三备份
3. min.insync.replicas = 2，大于1，消息至少要被写入到这么多副本才算成功，ack=all时有效
4. replication.factor > min.insync.replicas

**kafka消费者端：**

1. enable.auto.commit=false，关闭自动提交位移
2. 使用assgin不触发rebalance机制，每个client只处理一个partition线程，从而不触发rebalance机制
3. 消息处理完成之后再手动提交位移
4. 每个消费者绑定一个partition，因为同一个table不会跨partition存储，从而保证消息有序
