# （LeetCode练习题）堆


**题目**
- LeetCode 347. Top K Frequent Elements 前 K 个高频元素
- LeetCode 703. Kth Largest Element in a Stream 数据流中的第 K 大元素

**思路**

LeetCode 347. Top K Frequent Elements 前 K 个高频元素

```
先通过Map统计出每个数字出现的次数，然后通过对value从大到小排序维护一个大小为k的堆，依次存入元素，最后返回k的堆中元素即可  
当然还可以使用桶排序，每一个词频对应一个桶，这种方式时间复杂度为O(n)，但空间占用会更大一些  
时间复杂度：O(n*log(k))  
空间复杂度：O(n)
```

LeetCode 703. Kth Largest Element in a Stream 数据流中的第 K 大元素

```
使用最小堆，大小为k，堆顶元素即为第k大的元素  
时间复杂度：O(n*log(k))  
空间复杂度：O(k)
```
