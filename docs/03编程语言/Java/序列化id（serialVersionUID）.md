
1）对于类路径和实现代码相同的类，如果serialVersionUID不一样，则反序列化也会失败。

2）如果serialVersionUID一样，即使增加或删除了属性，依然可以反序列化，不会报错，对于删除的字段，则无法拿到，对于新增的字段，则会赋默认值。除非修改了属性的类型，则会报InvalidClassException错误。

3）如果没定义serialVersionUID，则序列化时会使用一个自动生成的id，在类发生变化的时候，id会发生变化，所以修改类属性后反序列化会失败。
