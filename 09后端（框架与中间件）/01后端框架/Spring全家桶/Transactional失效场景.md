# Transactional失效场景


1、非public方法：@Transactional 应用在非 public 修饰的方法上

2、传播机制问题：@Transactional 注解属性 propagation 设置错误

3、同类调用：同一个类中方法调用，导致 @Transactional 失效

4、@Transactional 注解属性 rollbackFor 设置错误

5、异常被 catch 捕获导致 @Transactional 失效

6、数据库引擎不支持事务

参考：[一口气说出6种@Transactional注解的失效场景](https://juejin.cn/post/6844904096747503629)
