# ES与关系型数据库对应关系


| Elasticsearch | 关系型数据库 (RDBMS)  | 说明                                                          |
| ------------- | --------------- | ----------------------------------------------------------- |
| Cluster       | Database Server | ES 集群由多个节点组成，类似于 RDBMS 中的数据库服务器实例，负责存储和管理数据。                |
| Index         | Table           | ES 中的一个 Index 通常用于存储一类相似的文档，类似于 RDBMS 中的一个 Table 存储一类相似的记录。 |
| Document      | Row (Record)    | ES 中的 Document 是 Index 中的基本数据单元，类似于 RDBMS 中 Table 的一行记录。    |
| Field         | Column (Field)  | Document 中的 Field 对应于 Table 中的 Column，用于存储具体的数据项。           |

备注：

1、Type

在 Elasticsearch 6.x 及之前的版本中，Index 的概念与 RDBMS 中的 Database 更为相似，因为一个 Index 可以包含多个 Type（类型），每个 Type 类似于一个 RDBMS 中的 Table。

然而，随着 Elasticsearch 的发展，Types 的概念被逐步弃用（当前推荐的最佳实践是采用单索引单类型的结构），最终在 Elasticsearch 7.x 中被完全移除。这一变化使得 Index 的角色与 RDBMS 中的 Table 更为接近。

2、Index对应表的概念，Mapping对应表结构的概念。
