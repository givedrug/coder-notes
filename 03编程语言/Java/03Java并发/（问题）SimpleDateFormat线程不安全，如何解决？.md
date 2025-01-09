# （问题）SimpleDateFormat线程不安全，如何解决？


1、方法中使用局部变量，每次new一个

2、使用同步锁（性能较差）

3、使用TreadLocal

**4、使用Java8中的DateTimeFormatter（线程安全的）**

5、使用Hutool的DateUtil工具类
