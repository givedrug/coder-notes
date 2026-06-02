# （问题）Mapper接口的工作原理是什么？Mapper接口里的方法，参数不同时，方法能重载吗？


- Mapper 接口的全限名，就是映射文件中的 namespace 的值。
- Mapper 接口的方法名，就是映射文件中 MappedStatement的 id 值。
- Mapper 接口方法内的参数，就是传递给 sql 的参数。

Mapper 接口是没有实现类的，当调用接口方法时，`接口全限名+方法名`拼接字符串作为 key 值，可唯一定位一个 MappedStatement。

```
举例：com.mybatis3.mappers.StudentMapper.findStudentById，可以唯一找到 namespace 为com.mybatis3.mappers.StudentMapper下面id = findStudentById的MappedStatement。
```

在 Mybatis 中，每一个`<select>`、`<insert>`、`<update>`、`<delete>`标签，都会被解析为一个 MappedStatement 对象。  

Mapper 接口里的方法，是不能重载的，因为是`接口全限名+方法名`的保存和寻找策略。并没有保存参数信息。  

Mapper 接口的工作原理是 JDK 动态代理，Mybatis 运行时会使用 JDK 动态代理为 Mapper 接口生成代理 proxy 对象，代理对象 proxy 会拦截接口方法，转而执行 MappedStatement 所代表的 sql，然后将 sql 执行结果返回。
