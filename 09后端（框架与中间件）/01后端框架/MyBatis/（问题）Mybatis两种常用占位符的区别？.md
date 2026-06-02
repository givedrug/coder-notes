# （问题）Mybatis两种常用占位符的区别？


Mybatis两种常用的占位符是`#{}`和`${}`，他们之间的区别是：

1、含义  

`#{}`解析为一个JDBC预编译语句（prepared statement）的参数标记符，会替换为`?`。  

```sql
select * from user where name = #{name};  
```

解析为：  

```sql
select * from user where name = ?;  
```

`${}`仅仅为一个纯碎的 string 替换，在动态 SQL 解析阶段将会进行变量替换，所以如果使用，需要自己加引号  

```sql
select * from user where name = '${name}';  
```

2、使用`#{}`可以有效的防止SQL注入，提高系统安全性。原因在于：预编译机制。预编译完成之后，SQL 的结构已经固定，即便用户输入非法参数，也不会对 SQL 的结构产生影响，从而避免了潜在的安全风险。  
  
3、使用建议：  能使用`#{}`的地方就用`#{}`，但表名作为变量时，必须使用`${}`。

```sql
select * from #{tableName} where name = #{name};

-- 用#{}：sql语句错误, select * from 'user' where name ='mary';

-- 用${}：sql语句正确, select * from user where name ='mary';
```
