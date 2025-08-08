# （问题）Runnalbe和Callable有什么区别？


1、返回值

Runnable是不返还值的，而Callable可以返回值。

2、异常响应

Runnable的run()方法定义没有抛出任何异常，所以任何的Checked Exception都需要在run()实现方法中自行处理。

Callable的Call()方法抛出了throws Exception，所以可以在call()方法的外部，捕捉到Checked Exception。

3、提交到线程池

execute()参数Runnable；

submit()参数(Runnable)或(Runnable和结果T)或(Callable)；submit()的返回值Future调用get方法时，可以捕获处理异常，Future的get()方法会阻塞当前线程直到任务完成。
