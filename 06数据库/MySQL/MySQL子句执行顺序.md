# MySQL子句执行顺序


SQL Select语句完整的执行顺序：

1. from子句组装来自不同数据源的数据；（先join在on）
2. where子句基于指定的条件对记录行进行筛选；
3. group by子句将数据划分为多个分组；
4. 使用聚集函数进行计算；
5. 使用having子句筛选分组；
6. 计算所有的表达式；
7. select 的字段；
8. 使用order by对结果集进行排序。

- (7) - SELECT
- (8) - DISTINCT <select_list>
- (1) - FROM <left_table>
- (3) - <join_type> JOIN <right_table>
- (2) - ON <join_condition>
- (4) - WHERE <where_condition>
- (5) - GROUP BY <group_by_list>
- (6) - HAVING <having_condition>
- (9) - ORDER BY <order_by_condition>
- (10) - LIMIT <limit_number>

关于 SQL 语句的执行顺序，有三个值得我们注意的地方：

1. FROM 才是 SQL 语句执行的第一步，并非 SELECT。 数据库在执行 SQL 语句的第一步是将数据从硬盘加载到数据缓冲区中，以便对这些数据进行操作。
2. SELECT 是在大部分语句执行了之后才执行的，严格的说是在 FROM 和 GROUP BY 之后执行的。理解这一点是非常重要的，这就是你不能在 WHERE 中使用在 SELECT 中设定别名的字段作为判断条件的原因。
3. 无论在语法上还是在执行顺序上， UNION 总是排在在 ORDER BY 之前。很多人认为每个 UNION 段都能使用 ORDER BY 排序，但是根据 SQL 语言标准和各个数据库 SQL 的执行差异来看，这并不是真的。尽管某些数据库允许 SQL 语句对子查询（subqueries）或者派生表（derived tables）进行排序，但是这并不说明这个排序在 UNION 操作过后仍保持排序后的顺序。
