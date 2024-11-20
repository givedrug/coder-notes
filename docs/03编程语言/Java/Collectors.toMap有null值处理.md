
参考：[https://stackoverflow.com/questions/24630963/nullpointerexception-in-collectors-tomap-with-null-entry-values](https://stackoverflow.com/questions/24630963/nullpointerexception-in-collectors-tomap-with-null-entry-values)

修改为：

HashMap::new, (map,entry)->map.put(entry.getKey(),entry.getValue()), HashMap::putAll

或者foreach
