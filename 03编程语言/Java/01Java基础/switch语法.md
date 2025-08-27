# switch语法


```java
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}
```

说明：
1. 从 expression 符合 case 后面的值处，开始执行代码，遇到 break 停止。如果没有 break，则会执行后面所有代码（default 也同样会执行）。
2. 如果 expression 没有符合的 case 值，则执行 default 中的语句。
3. switch 并不是所有类型都支持，目前支持的类型包括：
   基本数据类型：byte, short, char, int
   包装数据类型：Byte, Short, Character, Integer
   枚举类型：Enum
   字符串类型：String（Jdk 7+ 开始支持）

## SwitchInt.java

```java
public class SwitchInt {
    public static void main(String[] args) {
        int i = 1;
        switch (i) {
            case 0:
                System.out.println("0");
                break;
            case 1:
                System.out.println("1");
                break;
            default:
                System.out.println("default");
        }
    }
}
// 输出 1
```

## SwitchString.java

```java
public class SwitchString {
    public static void main(String[] args) {
        String color = "blue";
        switch (color) {
            case "blue":
                System.out.println("blue");
                break;
            case "red":
                System.out.println("red");
                break;
            default:
                System.out.println("invalid color");
        }
    }
}
// 输出 blue
// switch String 只能在 java7 或更高版本中使用
```

## SwitchEnum.java

```java
public class SwitchEnum {
    public static void main(String[] args) {
        Color color = Color.RED;
        switch (color) {
            case BLUE:
                System.out.println("blue");
                break;
            case RED:
                System.out.println("red");
                break;
            default:
                System.out.println("invalid color");
        }
    }

    enum Color {
        BLUE, RED
    }
}
// 输出 red
```
