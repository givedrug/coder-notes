# MySQL存储引擎介绍


MySQL 支持的引擎包括：InnoDB、MyISAM、MEMORY、Archive、Federate、CSV、BLACKHOLE等，其中较为常用的有三种：InnoDB、MyISAM、MEMORY。

InnoDB：是 MySQL 默认的存储引擎，支持事务处理，行级锁定和外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择 InnoDB 有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。

MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择 MyISAM 能实现处理高效率。如果应用的完整性、并发性要求比较低，也可以使用。

MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，对数据的安全性要求较低，可以选择 MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。

|                                                   | MyISAM    | Memory    | InnoDB   |
| ------------------------------------------------- | --------- | --------- | -------- |
| **B-tree indexes B树索引**                           | **Yes**   | **Yes**   | **Yes**  |
| Cluster database support 集群数据库支持                  | No        | No        | No       |
| **Clustered indexes 聚簇索引**                        | **No**    | **No**    | **Yes**  |
| Compressed data 压缩数据                              | Yes       | No        | Yes      |
| Data caches 数据缓存                                  | No        | N/A       | Yes      |
| Encrypted data 加密数据                               | Yes       | Yes       | Yes      |
| **Foreign key support 外键支持**                      | **No**    | **No**    | **Yes**  |
| Full-text search indexes 全文搜索索引                   | Yes       | No        | Yes      |
| Geospatial indexing support 地理空间索引支持              | Yes       | No        | Yes      |
| Hash indexes 哈希索引                                 | No        | Yes       | No       |
| Index caches 索引缓存                                 | Yes       | N/A       | Yes      |
| **Locking granularity 锁粒度**                       | **Table** | **Table** | **Row**  |
| **MVCC MVCC**                                     | **No**    | **No**    | **Yes**  |
| Replication support 复制支持                          | Yes       | Limited   | Yes      |
| **Storage limits 存储限制**                           | **256TB** | **RAM**   | **64TB** |
| T-tree indexes T树索引                               | No        | No        | No       |
| **Transactions 事务**                               | **No**    | **No**    | **Yes**  |
| Update statistics for data dictionary 更新数据字典的统计信息 | Yes       | Yes       | Yes      |

参考：https://dev.mysql.com/doc/refman/8.4/en/storage-engines.html
