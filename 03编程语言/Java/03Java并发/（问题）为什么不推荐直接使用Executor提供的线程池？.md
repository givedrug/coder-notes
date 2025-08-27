# （问题）为什么不推荐直接使用Executor提供的线程池？


FixedThreadPool、SingleThreadExecutor、CachedThreadPool、ScheduledThreadPool等，允许创建的线程数量为 Integer.MAX_VALUE ，可能会创建大量线程，从而导致OOM。

推荐通过ThreadPoolExecutor构造函数来创建，它提供了丰富的可设置的线程池构造参数，更适合对多线程进行管控。
