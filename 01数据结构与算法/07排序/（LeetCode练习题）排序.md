# （LeetCode练习题）排序


**题目**
- LeetCode LCR 164. 破解闯关密码
- LeetCode 75. Sort Colors 颜色分类
- LeetCode 147. Insertion Sort List 对链表进行插入排序
- LeetCode 164. Maximum Gap 最大间距
- LeetCode 215. Kth Largest Element in an Array 数组中的第K个最大元素
- LeetCode 283. Move Zeroes 移动零
- LeetCode 506. Relative Ranks 相对名次
- LeetCode 912. Sort an Array 排序数组
- LeetCode 1051. Height Checker 高度检查器
- LeetCode 1122. Relative Sort Array 数组的相对排序
- LeetCode 面试题 10.01. Sorted Merge LCCI 合并排序的数组

**思路**

LeetCode LCR 164. 破解闯关密码

```
两个数字排序规则为
1）依次比较每个位上的数字，如果某位数字不同，则小的在前，大的在后
2）如果耗尽某个数字所有位数，则在其后补充该数字的第一位的数字，然后按规则1进行比较
3）如果耗尽两个数字所有位数（按规则2补充后的），仍没有对比出大小，则返回(a + b)与(b + a)的字典序

查看题解，发现自己想复杂了，其实任意两个数字，直接比较(a + b)与(b + a)的字典序即可，
但我最开始的想法也有一点优势，就是占空间小一些，因为java字符串拼接会额外申请空间
复杂度：O(n*log(n))
```

LeetCode 75. Sort Colors 颜色分类

```
设置两个指针（类似于双轴快排）left表示0的右边界+1，right表示2的左边界-1
遍历数组，如果当前元素是0，则交换left和i，如果当前元素是2，则交换right和i，i--，否则i++
时间复杂度：O(n)
空间复杂度：O(1)
```

LeetCode 147. Insertion Sort List 对链表进行插入排序

```
使用两层遍历，外层为逐个遍历插入的元素，内层为找到应该插入的位置
复杂度：O(n^2)
```

LeetCode 164. Maximum Gap 最大间距

```
先基数排序（或者桶排序，因为有时间复杂度要求），然后找到最大间距
时间复杂度：O(n)
空间复杂度：O(n)
```

LeetCode 215. Kth Largest Element in an Array 数组中的第K个最大元素

```
方法一：先排序，然后返回第k个元素，时间复杂度为O(n*log(n))

方法二：效仿快速排序的思想，将数组根据某个值x划分，使得左侧都小于等于x，右侧都大于等于x，这样如果左侧个数为k-1的话，就可以返回x，否则遍历左边或者右边
注意，这里的时间复杂度其实不太容易得出，可参考《算法导论》，最坏的情况下为n^2，随机数据下为n

方法三：使用堆排序
复杂度：O(n)
```

LeetCode 283. Move Zeroes 移动零

```
方法一：冒泡方式，复杂度O(n^2)

方法二：双指针，左右指针中间皆为0，复杂度O(n)
```

LeetCode 506. Relative Ranks 相对名次

```
数字转为对象后排序并更新rank信息，对象排序后可以保留引用关系，直接遍历原列表根据rank值输出结果字符串数组
或者先排序，然后通过map保存rank映射（通过查找排名复杂度为O(n)），注意不要直接在排序后列表中查找排名，那样复杂度会升高为O(n^2)。
复杂度：O(n*log(n))
```

LeetCode 912. Sort an Array 排序数组

```
快排（或者直接使用计数排序，可以获得O(n)的时间复杂度）
复杂度：O(n*log(n))
```

LeetCode 1051. Height Checker 高度检查器

```
直接排序，然后逐项对比。因为元素范围比较小只有100个，所以使用计数排序可以获得O(n)的排序时间。
时间复杂度：O(n)
空间复杂度：O(n+k)
```

LeetCode 1122. Relative Sort Array 数组的相对排序

```
遍历arr1，统计arr2中每个数字出现的次数，不在arr2中的数字加入一个list中，然后按要求输出到结果中
时间复杂度：O(n)
空间复杂度：O(n)
```

LeetCode 面试题 10.01. Sorted Merge LCCI 合并排序的数组

```
逆向双指针，从后向前遍历，这样可以节省空间，另外，最后只需要处理A先结束的情况，如果B先结束则无需处理
时间复杂度：O(m+n)
空间复杂度：O(1)
```
