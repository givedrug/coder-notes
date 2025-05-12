# Spring生命周期


1、spring 容器初始化

- spring 容器实例化，扫描符合 Spring 规则的类（如 @Component、@Service 等注解或在 XML / Java Config 中配置的类），放入一个 list 集合中
- 遍历 list，继而把每个 class 封装为一个 beanDefinition 对象。每个 beanDefinition 对象都放入一个 map 中（beanFactory 中的 beanDefinitionMap）

1.5、实现接口 BeanFactoryPostProcessor 进行后置处理

- 先执行内置的一些处理
- 可以在实例化前，调用BeanFactoryPostProcessor拿到beanFactory中的某个类的BeanDefinition对象，从而改变这个bean的定义规则

2、实例化对象（构造函数）

- 从 beanDefinitionMap 依次取出 beanDefinition 进行验证（是否单例，是否非懒加载等）
- 推断 class 使用哪个构造方法
- 通过反射实例化对象
- 缓存注解信息，合并 beanDefinition（在某些场景下，Spring 会将子类与父类的 BeanDefinition 进行合并）
- 通过二级缓存暴露一个工厂 bean 对象或早期 bean

3、依赖注入

- 完成属性注入（Setter 注入、构造函数注入、字段注入等）
- 三级缓存（解决循环依赖）

```
singletonObjects 一级缓存，完整的 bean
singletonFactories 二级缓存，存的是代理 bean 工厂
earlySingletonObjects 三级缓存，一般是是半成品的 bean
```

3.5、回调部分 Aware 接口

- BeanNameAware：注入 Bean 的名称
- BeanFactoryAware：注入当前使用的 BeanFactory
- ApplicationContextAware：注入当前使用的 ApplicationContext 等

4、执行初始化函数

- 执行 BeanPostProcessor 前置处理
- 不同初始化方法的执行顺序：@postConstruct -> 实现 InitializingBean 初始化类 -> xml 中 init-method
- 执行 BeanPostProcessor 后置处理

5、BeanPostProcessor 代理（AOP）

- 如果实现了接口，则使用 jdk 动态代理实现，如果没有实现接口，则使用 cglib 实现代理，当然也可以指定都使用 cglib（jdk 动态代理使用反射实现；cglib 使用 asm 字节码操作库实现）
- 事件分发、发布监听

6、放入 bean 池（单例池或 spring 容器，也即一级缓存）

- Spring自动完成
- 手动放入单例池：ApplicationContext 上下文中调用 `getBeanFactory().registerSingleton`(beanName，对象)

7、销毁对象

- 执行顺序：@PreDestory -> DisposableBean 接口 -> destroy-method
