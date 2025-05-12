# （LeetCode练习题）链表


**题目**
- LeetCode 23. Merge k Sorted Lists 合并 K 个升序链表
- LeetCode 24. Swap Nodes in Pairs 两两交换链表中的节点
- LeetCode 82. Remove Duplicates from Sorted List II 删除排序链表中的重复元素 II
- LeetCode 138. Copy List with Random Pointer 复制带随机指针的链表
- LeetCode 142. Linked List Cycle II 环形链表 II
- LeetCode 203. Remove Linked List Elements 移除链表元素
- LeetCode 206. Reverse Linked List 反转链表
- LeetCode 328. Odd Even Linked List 奇偶链表
- LeetCode 430. Flatten a Multilevel Doubly Linked List 扁平化多级双向链表
- LeetCode 1290. Convert Binary Number in a Linked List to Integer 二进制链表转整数
- LeetCode 1472. Design Browser History 设计浏览器历史记录

**思路**

LeetCode 23. Merge k Sorted Lists 合并 K 个升序链表

```
使用小顶堆存储k个list的当前node，每次从小顶堆中取出最小值，放入新链表，如果这个最小值节点有next，再放入小顶堆，直到堆空；另外，还可以使用分治法。
复杂度：n*log(k)
```

LeetCode 24. Swap Nodes in Pairs 两两交换链表中的节点

```
顺序遍历，两两交换
复杂度：n
```

LeetCode 82. Remove Duplicates from Sorted List II 删除排序链表中的重复元素 II

```
虚拟头结点以及双指针
复杂度：n
```

LeetCode 138. Copy List with Random Pointer 复制带随机指针的链表

```
方法一：使用hash表，保存新旧节点映射关系。然后遍历处理即可。
时间复杂度：n
空间复杂度：n

方法二：官方解答中，还有一种空间复杂度为1的方法：
首先，将该链表中每一个节点拆分为两个相连的节点，例如对于链表A→B→C，我们可以将其变化为A→A′→B→B′→C→C′。
对于任意一个原节点S，其拷贝节点S′即为其后继节点。
然后，我们可以直接找到每一个拷贝节点S′的随机指针应当指向的节点，即为其原节点S的随机指针指向的节点T的后继节点T′。
最后，再遍历一遍，将其拆分即可。（需要注意原节点的随机指针可能为空，我们需要特别判断这种情况。）
时间复杂度：n
空间复杂度：1
```

LeetCode 142. Linked List Cycle II 环形链表 II

```
方法一：双指针：
第一次遍历，先通过快慢指针找到环，然后在环内遍历出环的大小len。
第二次遍历，再用间隔为len的两个指针重新遍历，相遇出即为环入口。
时间复杂度：n
空间复杂度：1

方法二：官方解答中，还有一种更为简练的方法，当快慢指针相遇时，再引入第三个指针，然后同时移动快/慢指针与第三个指针，它们将在环入口相遇（可数学证明）
时间复杂度：n
空间复杂度：1
```

LeetCode 203. Remove Linked List Elements 移除链表元素

```
可以直接遍历处理；另外，还可以通过递归处理。
复杂度：n
```

LeetCode 206. Reverse Linked List 反转链表

```
快中慢三指针；还可以遍历当前指针，并用头插法插入新list；官方解答中还有一种递归方式，虽然空间复杂度为n，但形式简单。
复杂度：时间n、空间1
```

LeetCode 328. Odd Even Linked List 奇偶链表

```
维护两个list，一个奇数一个偶数，然后连接
复杂度：n
```

LeetCode 430. Flatten a Multilevel Doubly Linked List 扁平化多级双向链表

```
本质是在在树上遍历，prev相当于指向父节点，child相当于左孩子，next相当于右孩子，将所有节点合并进右侧
可采用深度优先算法，从head开始遍历，当前层级中间节点（非尾节点）带child时，递归处理，当前层级尾节点带child时，将其摆直后继续遍历
复杂度：时间n、空间d（层数）
```

LeetCode 1290. Convert Binary Number in a Linked List to Integer 二进制链表转整数

```
方法一：转换为字符串，然后转进制
复杂度：n

方法二：官方解答中可以一边遍历一遍计算，只需让原来的数字乘2加上现在的数字即可
复杂度：n
```

LeetCode 1472. Design Browser History 设计浏览器历史记录

```
链表（还可以通过hash表实现，key是index，value是url）。
备注：题目中有一点没有说清楚，就是当前index如果在中间时，插入url后，url会覆盖index+1的位置，并且大于index+1的位置也都作废不能访问。
复杂度：-
```
