
```java
Pattern p = Pattern.compile(":[a-zA-Z]+");
Matcher m = p.matcher("This is a :test string with :another example:123");
while (m.find()) {
    System.out.println(m.group());
}
```

输入：

```
This is a :test string with :another example:123
```

输出：

```
:test
:another
```
