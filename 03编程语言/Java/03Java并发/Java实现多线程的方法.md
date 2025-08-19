# Java实现多线程的方法


实现Runnable接口：

```java
public class RunnableStyle implements Runnable{

    public static void main(String[] args) {
        Thread thread = new Thread(new RunnableStyle());
        thread.start();
    }

    public void run() {
        System.out.println("使用Runnable方式创建多线程");
    }
}
```

继承Thread类：

```java
public class ThreadStyle extends Thread{

    @Override
    public void run() {
        System.out.println("使用Thread方式创建多线程");
    }

    public static void main(String[] args) {
        new ThreadStyle().start();
    }
}
```

## 两种方法对比

1. 从代码结构看，Runnable表示实际的操作，和Thread解耦后代码更清晰。
2. 从系统开销看，Thread方式开销较大，使用Runnable可以利用线程池方式，节约资源。
3. 从扩展性看，Runnable是接口，可以再实现其他接口，或继承某个类，但Java不支持双继承，所以Thread不能再继承其他类。

推荐使用 implements Runnable 方式，当然，java和各种工具库针对各种场景提供了诸如线程池等方式来创建和管理多线程，一般不需要自己手动实现 Runnable 来创建。

## 两种方法本质

Thread中的run方法实际执行的是Thread中一个Runnable类型的局部变量target的run方法：  

1.（Runnable方式）如果Thread初始化时传入了Runnable类型的参数，则执行这个参数的run方法

2.（Thread方式）如果重写了Thread的run方法，那就直接执行重写后的方法

```java
@Override
public void run() {
    if (target != null) {
        target.run();
    }
}
```

一些错误观点：

1. 线程池创建线程也算是一种新建线程的方式
2. 通过Callable和FutureTask创建线程，也是一种新的创建线程方式
3. 无返回值是Runnable，有返回值是Callable，所以Callable是新的实现线程的方式
4. 定时器方式
5. 匿名内部类
6. Lambda表达式（只是语法包装）

他们本质上都是使用了 Runnable 方式。
