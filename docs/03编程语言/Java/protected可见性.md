
基类的protected成员是包内可见的，并且对包内子类可见；

若子类与基类不在同一包中，那么在子类中，子类实例可以访问其从基类继承而来的protected方法，而我们不能通过基类实例访问基类的protected方法。

```java
package p1;

class MyObject {

    protected int test() {
       return 1;
    }

}

package p2;

public class SonObject extends MyObject {

    public static void main(String args[]) {
       MyObject2 obj = new MyObject();//生成父类实例对象
       obj.test(); // Compile Error        
       SonObject tobj = new SonObject();//生成子类实例对象
       tobj.test(); // Complie OK       
    }

}
```
