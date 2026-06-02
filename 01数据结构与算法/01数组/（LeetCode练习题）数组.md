# （LeetCode练习题）数组


**题目**
- LeetCode 35. Search Insert Position 搜索插入位置
- LeetCode 48. Rotate Image 旋转图像
- LeetCode 56. Merge Intervals 合并区间
- LeetCode 485. Max Consecutive Ones 最大连续 1 的个数
- LeetCode 498. Diagonal Traverse 对角线遍历
- LeetCode 1991. Find the Middle Index in Array 找到数组的中间位置
- LeetCode 面试题 01.08. Zero Matrix LCCI 零矩阵

**思路**

LeetCode 35. Search Insert Position 搜索插入位置

```
二分查找
复杂度：log(n)
```

LeetCode 48. Rotate Image 旋转图像

```
直接交换四分之一块(i,j)->(j,n-i)
复杂度：n^2
```

LeetCode 56. Merge Intervals 合并区间

```
先排序，然后两两合并
复杂度：n
```

LeetCode 485. Max Consecutive Ones 最大连续 1 的个数

```
顺序遍历，记录连续1个数
复杂度：n
```

LeetCode 498. Diagonal Traverse 对角线遍历

```
注意到，每次同一条对角线上的坐标(i,j)都有i+j为固定值，且下一条比上一条递增1（注意奇数行与偶数行要调换顺序）
复杂度：m*n
```

LeetCode 1991. Find the Middle Index in Array 找到数组的中间位置

```
先求和，然后遍历数组，同时对比左右子数组的和
复杂度：n
```

LeetCode 面试题 01.08. Zero Matrix LCCI 零矩阵

```
第一遍找出所有0元素的行号与列号，第二遍置零
复杂度：m*n
```
