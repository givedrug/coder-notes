# （问题）有哪些SQL性能分析工具？


**show命令**

```sql
show status ——显示状态信息（扩展show status like ‘XXX’）
show variables ——显示系统变量（扩展show variables like ‘XXX’）
show innodb status ——显示InnoDB存储引擎的状态
show processlist ——查看当前SQL执行，包括执行状态、是否锁表等
```

**慢查询日志**

默认情况下，MySQL数据库没有开启慢查询日志，需要手动设置参数开启。（long_query_time的默认值为10，意思是运行10秒以上的语句）

MySQL提供了日志分析工具mysqldumpslow。

**执行计划**

TYPE（类型性能是依次降低的）：

- system，这是const连接类型的一个特例，当查询的表只有一行时使用。
- const，表中有且只有一个匹配的行时使用，如对主键或是唯一索引的查询，这是效率最高的联接方式。
- eq_ref，唯一索引或者是主键索引查找，对于每个索引键，表中只有一条记录与之匹配
- ref，非唯一索引查找，返回匹配某个单独值的所有行。
- ref_or_null，类似于ref类型的查询，但是附加了对NULL值列的查询。
- index_merge，该联接类型表示使用了索引合并优化方法。
- range，索引范围扫描，常见于between、>、<、这样的查询条件。
- index，full index scan 全索引扫描，同ALL的区别是，遍历的是索引树。
- all，full table scan 全表扫描，这是效率最差的联接方式。

Extra（包含不适合在其他列中显示但十分重要的额外信息）：
- using filesort:说明mysql会对数据使用一个外部的索引排序，不是按照表内的索引顺序进行读取。mysql中无法利用索引完成的排序操作称为“文件排序”。常见于order by和group by语句中
- using temporary：使用了临时表保存中间结果，mysql在对查询结果排序时使用临时表。常见于排序order by和分组查询group by。
- using index：表示相应的select操作中使用了**覆盖索引**，避免访问了表的数据行，效率不错，如果同时出现using where，表明索引被用来执行索引键值的查找；否则索引被用来读取数据而非执行查找操作

**Show Profile分析**

Show Profile是MySQL提供可以用来分析当前会话中语句执行的资源消耗情况。
