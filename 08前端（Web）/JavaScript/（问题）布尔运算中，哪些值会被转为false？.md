# （问题）布尔运算中，哪些值会被转为false？


在 JavaScript（以及很多语言的相似逻辑中）进行布尔值转换（也称为“类型转换”）时，确实只有如下 6 个值会被视为`false`：

1. `undefined`
2. `null`
3. `false`
4. `0`（包括 `-0`）
5. `NaN`
6. `""` 或 `''`（空字符串）

**除此之外，所有其他值都被视为`true`。**

示例：

```
Boolean(undefined) -> false
Boolean(null) -> false
Boolean(false) -> false
Boolean(0) -> false
Boolean(NaN) -> false
Boolean("") -> false
Boolean("0") -> true （字符串 "0" != 数字 0）
Boolean([]) -> true （空数组）
Boolean({}) -> true （空对象）
Boolean(" ") -> true （非空字符串，尽管只含空格）
```
