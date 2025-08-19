# （LeetCode练习题）哈希表


**题目**
- LeetCode 36. Valid Sudoku 有效的数独
- LeetCode 49. Group Anagrams 字母异位词分组
- LeetCode 169. Majority Element 多数元素
- LeetCode 202. Happy Number 快乐数
- LeetCode 205. Isomorphic Strings 同构字符串
- LeetCode 287. Find the Duplicate Number 寻找重复数
- LeetCode 349. Intersection of Two Arrays 两个数组的交集
- LeetCode 350. Intersection of Two Arrays II 两个数组的交集 II
- LeetCode 387. First Unique Character in a String 字符串中的第一个唯一字符
- LeetCode 454. 4Sum II 四数相加 II
- LeetCode 705. Design HashSet 设计哈希集合
- LeetCode 706. Design HashMap 设计哈希映射
- （困难）LeetCode 146. LRU Cache LRU 缓存
- （困难）LeetCode 380. Insert Delete GetRandom O(1) O(1) 时间插入、删除和获取随机元素
- （困难）LeetCode 460. LFU Cache LFU 缓存

**思路**

LeetCode 36. Valid Sudoku 有效的数独

```
方法一：分别按行、按列、按九宫遍历
复杂度：1（遍历次数为常数）

方法二：官方解答中，也可以把三次遍历转为一次遍历，并同时记录三种条件下的重复情况
复杂度：1（遍历次数为常数）
```

LeetCode 49. Group Anagrams 字母异位词分组

```
生成每个字符串的排序后字符串，通过hash表做映射
复杂度：n*m*log(m)
```

LeetCode 169. Majority Element 多数元素

```
通过map统计每个数字出现个数，然后返回个数最大的数字
复杂度：n
```

LeetCode 202. Happy Number 快乐数

```
方法一：使用HashSet
复杂度：log(n)

方法二：官方解答还提出可以使用快慢指针来实现，等价于找到链表是否有环
复杂度：log(n)
```

LeetCode 205. Isomorphic Strings 同构字符串

```
保存两字符串的对应字符的映射关系，注意要保留相互两份映射
复杂度：n
```

LeetCode 287. Find the Duplicate Number 寻找重复数

```
方法一：使用HashSet
时间复杂度：n
空间复杂度：n

方法二：官方解答中提到了一种时间n、空间1的方法，双指针法。
首先将数组构造成链表（必然有环）index->nums[index]
0 1 2 3 4
1 3 4 2 2
链表为：0->1->3->2->4(->2成环)

简单证明为什么一定成环：
首先0作为起点，只会指向别的节点，不会有节点指向0
这样（除去0）index就有n个，而被指向的节点共有n+1个
所以必然有一个节点至少被从两个位置指向（包括自指向）

注意：不一定只有一个环，但从0出发的一定能找到有且一个环，如下例子：
0 1 2 3 4
1 2 2 4 3
链表为：0->1->2(->2自成环)
3->4(->3成第二个环)

这样构造出从0出发的一定有一个环的链表，且环入口就是重复元素，就可以使用快慢指针来找到了
而且这个链表并不一定要真正的构造出来，index和nums[index]的关系已经足够。

时间复杂度：n
空间复杂度：1
```

LeetCode 349. Intersection of Two Arrays 两个数组的交集

```
使用HashSet
复杂度：n
```

LeetCode 350. Intersection of Two Arrays II 两个数组的交集 II

```
使用HashMap，计数
复杂度：n
```

LeetCode 387. First Unique Character in a String 字符串中的第一个唯一字符

```
使用map计数，还可以使用Ascii码数组计数，速度更快
复杂度：n
```

LeetCode 454. 4Sum II 四数相加 II

```
分别计算数组1、2和数组3、4的所有和的统计结果map，然后遍历和为0的计数。另外，如果数组重复值多的话，还可以继续优化，先统计数字出现个数，再生成统计map
复杂度：n^2
```

LeetCode 705. Design HashSet 设计哈希集合

```
使用一个数组存数据，数组元素是一个链表表头，该链表下所有key的hash值相等。
另外，这里只是给出一个最简单的hashSet实现，如果要进行优化，可以从下面几点考虑：
1）hash函数，可以采用更优的散列函数。
2）链表改为树，参考Java内置HashMap的实现。
3）扩容机制，当元素个数过多时，可以对其进行扩容，降低hash冲突概率。
复杂度：>1
```

LeetCode 706. Design HashMap 设计哈希映射

```
与705相似
复杂度：>1
```

（困难）LeetCode 146. LRU Cache LRU 缓存

```
方法一：通过双向链表（目的是保存先后顺序）表示LRU，但查询复杂度为n，所以增加一个辅助hash表，使得查询复杂度降为1
复杂度：1

方法二：还可以借助java提供的LinkedHashMap来实现，它本身就是通过list+hash结合实现的
复杂度：1
```

（困难）LeetCode 380. Insert Delete GetRandom O(1) O(1) 时间插入、删除和获取随机元素

```
使用一个HashMap，一个ArrayList
复杂度：1
```

（困难）LeetCode 460. LFU Cache LFU 缓存

```
map-list-map方案：
首先建立一个hashmap，key是访问次数，value是一个linkedList，list内所有节点的访问次数是一样的，并按访问时间排序。
然后再建立一个hashmap，key是输入数据的key，value是上述list的节点，为了方便定位某个具体key-value数据。
最后再维护一个当前最小访问次数的变量，用户快速找到需要剔除的元素。
复杂度：1
```
