# （LeetCode练习题）字符串


**题目**
- LeetCode 14. Longest Common Prefix 最长公共前缀
- LeetCode 151. Reverse Words in a String 反转字符串中的单词
- LeetCode 557. Reverse Words in a String III 反转字符串中的单词 III
- （困难）LeetCode 5. Longest Palindromic Substring 最长回文子串
- （困难）LeetCode 28. Find the Index of the First Occurrence in a String 找出字符串中第一个匹配项的下标

**思路**

LeetCode 14. Longest Common Prefix 最长公共前缀

```
两两获取公共前缀，并使用公共前缀，遍历后续String，最终得到所有的公共前缀
复杂度：n（所有字符的个数）
```

LeetCode 151. Reverse Words in a String 反转字符串中的单词

```
顺序遍历，跳过空格，遇到非空格后记录单词，并将单词放入list，反序后join空格并返回
复杂度：n
```

LeetCode 557. Reverse Words in a String III 反转字符串中的单词 III

```
滑动窗口
复杂度：n
```

（困难）LeetCode 5. Longest Palindromic Substring 最长回文子串

```
方法一：暴力解法，遍历字符，分别将当前字符作为回文中心查找最大回文串（注意奇数回文与偶数回文的差异），复杂度O(n^2)
复杂度：n^2

方法二：Manacher算法
复杂度：n
```

（困难）LeetCode 28. Find the Index of the First Occurrence in a String 找出字符串中第一个匹配项的下标

```
方法一：暴力解法，遍历字符串，依次对比
复杂度：n*m

方法二：KMP算法
复杂度：n+m
```
