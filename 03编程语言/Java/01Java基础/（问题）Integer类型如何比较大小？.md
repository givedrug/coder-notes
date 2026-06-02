# （问题）Integer类型如何比较大小？


如果直接使用\=\=，在值不在-128~127范围（java有缓存）时，即使数值相等，也会返回false。

两种方法：

```java
public static boolean areIntegersEqual(Integer a, Integer b) {
    if (a == null && b == null) {
        return true;
    }
    if (a == null || b == null) {
        return false;
    }
    return a.equals(b);
}
```

或者一种更简洁的：

```java
import java.util.Objects;

Objects.equals(a, b);
```

Objects.equals() 方法会自动处理 null 值的情况，如果两个参数都为 null，它返回 true；如果只有一个为 null，返回 false；如果都不为 null，则调用 a.equals(b)。
