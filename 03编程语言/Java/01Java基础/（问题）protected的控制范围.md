# （问题）protected的控制范围


|           | 同类  | 同包  | 不同包-子类 | 不同包-非子类 |
| --------- | --- | --- | ------ | ------- |
| public    | Yes | Yes | Yes    | Yes     |
| protected | Yes | Yes | Yes    | No      |
| 默认        | Yes | Yes | No     | No      |
| private   | Yes | No  | No     | No      |

protected是允许在同一包内或继承关系中的子类中访问；

若子类与父类不在同一包中，那么在子类中，子类实例可以访问其从父类继承而来的protected方法（不同包-子类），而我们不能通过父类实例访问父类的protected方法（不同包-非子类）。

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
