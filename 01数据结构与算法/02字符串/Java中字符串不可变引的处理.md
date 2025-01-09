# Java中字符串不可变引的处理


在java中，字符串无法被修改。哪怕你只是想修改其中的一个字符，也必须创建一个新的字符串。

为了避免空间浪费，可以通过如下方案解决：

1、如果你确实希望你的字符串是可变的，则可以使用 toCharArray 将其转换为字符数组。

```java
String str="Hello World!";
        char[]strCharArray=str.toCharArray();
        strCharArray[5]=',';
        String newStr=new String(strCharArray);
        System.out.println(newStr);
// Hello,World!
```

2、如果你经常必须连接字符串，最好使用一些其他的数据结构，如StringBuilder或StringBuffer 。

StringBuffer：线程安全；速度较慢；多线程操作大量数据使用。

StringBuilder：线程不安全；速度较快；单线程操作大量数据使用。

String：操作少量的数据使用。
