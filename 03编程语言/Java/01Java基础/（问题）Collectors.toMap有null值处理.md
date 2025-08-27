# （问题）Collectors.toMap有null值处理


对于如下代码：

```java
class Answer {
    private int id;

    private Boolean answer;

	...	
}

public class Main {
    public static void main(String[] args) {
        List<Answer> answerList = new ArrayList<>();

        answerList.add(new Answer(1, true));
        answerList.add(new Answer(2, true));
        answerList.add(new Answer(3, null));

        Map<Integer, Boolean> answerMap =
        answerList.stream().collect(Collectors.toMap(Answer::getId, Answer::getAnswer));
    }
}
```

因为value中存在null值，所以会报NPE空指针错误。修改为：

```java
Map<Integer, Boolean> collect = list.stream()
        .collect(HashMap::new, (m,v)->m.put(v.getId(), v.getAnswer()), HashMap::putAll);
```

或者使用foreach：

```java
Map<Integer,  Boolean> answerMap = new HashMap<>();
answerList.forEach((answer) -> answerMap.put(answer.getId(), answer.getAnswer()));
```

```java
Map<Integer, Boolean> answerMap = new HashMap<>();
for (Answer answer : answerList) {
    answerMap.put(answer.getId(), answer.getAnswer());
}
```

参考：[https://stackoverflow.com/questions/24630963/nullpointerexception-in-collectors-tomap-with-null-entry-values](https://stackoverflow.com/questions/24630963/nullpointerexception-in-collectors-tomap-with-null-entry-values)
