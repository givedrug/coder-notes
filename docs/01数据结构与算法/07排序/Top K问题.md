
Top K问题是一类常见的算法问题，一般可以应用排序算法解决，通常是在一堆数字（或字符串）中找到第K大的数字（或最大的数字即Top 1）、找到前K大的数字（有序的或无序的）或者Top K词频等问题。依据数字串的特征、时间要求、空间要求以及其他限制条件，通常采取不同的处理方式。

**例子1**：如何在10亿个数中如何高效地找到最大的一个数？

解答：将10亿个数据分成1000份，每份100万个数据，找到每份数据中最大的那个数据，最后在剩下的1000个数据里面找出最大的数据。 从100万个数据遍历选择最大的数，此方法需要每次的内存空间为$10^6*4=4MB$，一共需要1000次这样的比较。由于只需要找到最大值，所以为线性时间复杂度。

**例子2**：如何在10亿个数中如何高效地找到第K大的数？

解答：通常使用分治（如Hash）+小顶堆。先将数据集切分（直接切分或使用Hash切分）成多个小数据集，然后用小顶堆求出每个数据集中前K大的数，最后在所有top K中求出最终的top K，最后一步可以仍然使用一个小顶堆，最后的堆顶元素即为第K大的数。

注意使用的是小顶堆而不是大顶堆，因为我们只需要取出前K大的数字，具体操作为：维护一个元素数为k的小顶堆，每次都将新的元素与堆顶元素（堆中最小的元素）进行比较，如果新的元素比堆顶元素大，则弹出堆顶元素，将新的元素添加进堆中，最终，堆中的k个元素即为前k大的元素。

耗时主要发生在对每组数据求前K大的数字，时间复杂度为$O(n \log k)$。

**例子3**：如何在10亿个字符串中找到词频前K大的字符串？

解答：通常使用分治+Trie树/HashMap+小顶堆。与例子2相似，先将数据集切分（直接切分或使用Hash切分）成多个小数据集，然后使用Trie树或者HashMap统计每个小数据集中的词频，之后用小顶堆求出每个数据集中出频率最高的前K个数，最后在所有top K中求出最终的top K个字符串。时间复杂度为$O(n \log k)$。

**一些常见的Top K问题处理方式：**

一个朴素的想法是，可以先对所有元素进行排序，然后即可方便的获取Top K的元素。这种方式对于数据规模较大的数据集，处理效率会非常低，通常不会使用此方法。取Top K的元素一般不需要全局有序，仅需要局部有序（如简单排序、二分插入、堆排序等），或者划分组之间有序（如partition法、桶排序等）即可。

**分治思想**：对于数据规模较大的数据集，通常采用先切分为小数据集，最后在合并处理的方式。分治的方法可以直接按条数或按最终小数据集的个数来切分，也可以通过Hash进行切分（比如需要将相同或某类元素放在同一个组，当然没有这个要求，也可以直接使用Hash切分）。

**Top K**：在切分后的数据集中，获取前K大的元素的有如下方法：
- 简单排序：可以通过冒泡排序或选择排序，获取前K个元素后停止，这样需要遍历全部元素K次，效率较低。
- 二分插入：先取K个元素进行排序，然后遍历剩余元素，二分查找后插入到已排序序列中，并淘汰最小值，最终获得前K大的元素，时间复杂度为$O(n \log k)$；
- 小顶堆：先取K个元素生成小顶堆，然后遍历剩余元素与堆顶元素（最小元素）进行比较，如果新元素比堆顶元素大，则弹出堆顶元素，将新元素添加进堆中，最终，堆中的k个元素即为前k大的元素，时间复杂度为$O(n \log k)$；
- partition法：借鉴快排的思想，选取一个基准值，将序列分为两组，一组小于等于基准值，一组大于基准值，通过这两组的元素个数与K的大小关系，递归的使用partition法，直到大于某个值的个数恰好为K时停止，时间复杂度为$O(n)$。这里基准值的选取很关键，可以随机获取，或者采样后选取中位数作为其值（比如BFPRT方法）。
- 桶排序：数据集成为多个buckets（桶之间有序），每一轮结束后，从大桶到小桶检查数据个数，并与K比较，以决定还需要对哪个桶（下一轮只需要递归一个桶）进行递归，每个bucket的排序可以使用其他算法也可以递归的使用桶排序。
- 计数排序：对于数据集中的数字范围不大时，可以使用计数排序，相同于划分了“数字范围”那么多个桶，从大到小进行求和计数即可获得前K元素。
- 基数排序：按整数位数从高到低进行排序，每轮排序完，可以检查大数到小数的数据个数，并于K比较，以决定还需要对哪个数字进行下一轮递归，最终获取前K个元素。

**词频统计**：通常使用HashMap或者Trie树（前缀树、字典树）进行词频统计，如果字符串的类型很大，那么直接使用HashMap将占用过多空间，这时应考虑使用Trie树来进行统计。如果是在动态流中，愿意牺牲一些准确性，而获取更高的词频统计效率，还可以考虑Count-min Sketch、Lossy Couting等算法。

参考：
1. [10亿个数中如何高效地找到最大的一个数以及最大的第K个数](https://github.com/weitingyuk/LeetCode-Notes-Waiting/blob/main/2021-02-17/TopK.md)
2. [Top K 频繁项](https://soulmachine.gitbooks.io/system-design/content/cn/bigdata/heavy-hitters.html)
3. [线性找第 k 大的数](https://oi-wiki.org/basic/quick-sort/#%E7%BA%BF%E6%80%A7%E6%89%BE%E7%AC%AC-k-%E5%A4%A7%E7%9A%84%E6%95%B0)
