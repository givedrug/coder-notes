# LFU缓存设计


**题目：**

请你为 LFU(Least Frequently Used 最不经常使用)缓存算法设计并实现数据结构。

实现 LFUCache 类：
- LFUCache(int capacity) 用数据结构的容量 capacity 初始化对象；
- int get(int key) 如果键 key 存在于缓存中，则获取键的值，否则返回 -1；
- void put(int key, int value) 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。

为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

```
示例

输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // 返回 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // 返回 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
```

**思路与代码：**

**方法一：哈希表 + 平衡二叉树**

由于主流语言中都有内置平衡二叉树，因此利用其进行自动排序从而实现 LFU 较为方便，但应注意其时间复杂度是 $O(log(n))$ 并非 $O(1)$ 。

首先我们定义缓存的数据结构，java中可以通过实现Comparable类来自定义比较函数：

```java
class Node implements Comparable<Node> {
    // cnt 表示缓存使用的频率，time 表示缓存的使用时间，key 和 value 表示缓存的键值
    int cnt, time, key, value;

    Node(int cnt, int time, int key, int value) {
        this.cnt = cnt;
        this.time = time;
        this.key = key;
        this.value = value;
    }

    public boolean equals(Object anObject) {
        if (this == anObject) {
            return true;
        }
        if (anObject instanceof Node) {
            Node rhs = (Node) anObject;
            return this.cnt == rhs.cnt && this.time == rhs.time;
        }
        return false;
    }

    // 比较函数：将cnt（使用频率）作为第一关键字，time（最近一次使用的时间）作为第二关键字
    public int compareTo(Node rhs) {
        return cnt == rhs.cnt ? time - rhs.time : cnt - rhs.cnt;
    }

    public int hashCode() {
        return cnt * 1000000007 + time;
    }
}
```

我们用哈希表 keyTable 以键 key 为索引存储缓存 Node，建立一个平衡二叉树 treeSet 来保持缓存根据 (cnt，time) 双关键字排序。
在 Java 中，我们可以使用 TreeSet 类，其背后的实现是红黑树（一种特化的AVL树即平衡二叉树）：

1）对于 get(key) 操作，我们只要查看一下哈希表 keyTable 是否有 key 这个键即可，有的话需要同时更新哈希表和集合中该缓存的使用频率以及使用时间，否则返回 -1。

2）对于 put(key, value) 操作，首先需要查看 keyTable 中是否已有对应的键值。如果有的话操作基本等同于 get(key)，不同的是需要更新缓存的 value 值。如果没有的话相当于是新插入一个缓存，这时候需要先查看是否达到缓存容量 capacity，如果达到了的话，需要删除最近最少使用的缓存，即平衡二叉树中最左边的结点，同时删除 keyTable 中对应的索引，最后向 keyTable 和 treeSet 插入新的缓存信息即可。

```java
class LFUCache {
    // 缓存容量，时间戳
    int capacity, time;
    Map<Integer, Node> keyTable;
    TreeSet<Node> treeSet;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.time = 0;
        keyTable = new HashMap<>();
        treeSet = new TreeSet<>();
    }

    public int get(int key) {
        if (capacity == 0) {
            return -1;
        }
        // 如果哈希表中没有键 key，返回 -1
        if (!keyTable.containsKey(key)) {
            return -1;
        }
        // 从哈希表中得到旧的缓存
        Node cache = keyTable.get(key);
        // 从平衡二叉树中删除旧的缓存
        treeSet.remove(cache);
        // 将旧缓存更新
        cache.cnt += 1;
        cache.time = ++time;
        // 将新缓存重新放入哈希表和平衡二叉树中
        treeSet.add(cache);
        keyTable.put(key, cache);
        return cache.value;
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (!keyTable.containsKey(key)) {
            // 如果到达缓存容量上限
            if (keyTable.size() == capacity) {
                // 从哈希表和平衡二叉树中删除最近最少使用的缓存
                keyTable.remove(treeSet.first().key);
                treeSet.remove(treeSet.first());
            }
            // 创建新的缓存
            Node cache = new Node(1, ++time, key, value);
            // 将新缓存放入哈希表和平衡二叉树中
            keyTable.put(key, cache);
            treeSet.add(cache);
        } else {
            // 这里和 get() 函数类似
            Node cache = keyTable.get(key);
            treeSet.remove(cache);
            cache.cnt += 1;
            cache.time = ++time;
            cache.value = value;
            treeSet.add(cache);
            keyTable.put(key, cache);
        }
    }
}
```

- 时间复杂度：get 时间复杂度 $O(\log n)$，put 时间复杂度 $O(\log n)$，操作的时间复杂度瓶颈在于平衡二叉树的插入删除均需要 $O(\log n)$ 的时间。
- 空间复杂度：$O(\textit{capacity})$，其中 capacity 为 LFU 的缓存容量。哈希表和平衡二叉树不会存放超过缓存容量的键值对。

**方法二：双哈希表**

我们定义两个哈希表，第一个 freqTable 以频率 freq 为索引，每个索引存放一个双向链表，这个链表里存放所有使用频率为 freq 的缓存，缓存里存放三个信息，分别为键 key，值 value，以及使用频率 freq。第二个 keyTable 以键值 key 为索引，每个索引存放对应缓存在 freqTable 中链表里的内存地址，这样我们就能利用两个哈希表来使得两个操作的时间复杂度均为 O(1)。同时需要记录一个当前缓存最少使用的频率 minFreq，这是为了删除操作服务的。

1）对于 get(key) 操作，我们能通过索引 key 在 keyTable 中找到缓存在 freqTable 中的链表的内存地址，如果不存在直接返回 -1，否则我们能获取到对应缓存的相关信息，这样我们就能知道缓存的键值还有使用频率，直接返回 key 对应的值即可。

但是我们注意到 get 操作后这个缓存的使用频率加一了，所以我们需要更新缓存在哈希表 freqTable 中的位置。已知这个缓存的键 key，值 value，以及使用频率 freq，那么该缓存应该存放到 freqTable 中 freq + 1 索引下的链表中。所以我们在当前链表中 O(1) 删除该缓存对应的节点，根据情况更新 minFreq 值，然后将其 O(1) 插入到 freq + 1 索引下的链表头完成更新。这其中的操作复杂度均为 O(1)。你可能会疑惑更新的时候为什么是插入到链表头，这其实是为了保证缓存在当前链表中从链表头到链表尾的插入时间是有序的，为下面的删除操作服务。

2）对于 put(key, value) 操作，我们先通过索引 key在 keyTable 中查看是否有对应的缓存，如果有的话，其实操作等价于 get(key) 操作，唯一的区别就是我们需要将当前的缓存里的值更新为 value。如果没有的话，相当于是新加入的缓存，如果缓存已经到达容量，需要先删除最近最少使用的缓存，再进行插入。

先考虑插入，由于是新插入的，所以缓存的使用频率一定是 1，所以我们将缓存的信息插入到 freqTable 中 1 索引下的列表头即可，同时更新 keyTable\[key\] 的信息，以及更新 minFreq = 1。

那么剩下的就是删除操作了，由于我们实时维护了 minFreq，所以我们能够知道 freqTable 里目前最少使用频率的索引，同时因为我们保证了链表中从链表头到链表尾的插入时间是有序的，所以 freqTable\[minFreq\] 的链表中链表尾的节点即为使用频率最小且插入时间最早的节点，我们删除它同时根据情况更新 minFreq ，整个时间复杂度均为 O(1) 。

```java
class LFUCache {
    int minfreq, capacity;
    Map<Integer, Node> keyTable;
    Map<Integer, DoublyLinkedList> freqTable;

    public LFUCache(int capacity) {
        this.minfreq = 0;
        this.capacity = capacity;
        keyTable = new HashMap<Integer, Node>();
        freqTable = new HashMap<Integer, DoublyLinkedList>();
    }
    
    public int get(int key) {
        if (capacity == 0) {
            return -1;
        }
        if (!keyTable.containsKey(key)) {
            return -1;
        }
        Node node = keyTable.get(key);
        int val = node.val, freq = node.freq;
        freqTable.get(freq).remove(node);
        // 如果当前链表为空，我们需要在哈希表中删除，且更新minFreq
        if (freqTable.get(freq).size == 0) {
            freqTable.remove(freq);
            if (minfreq == freq) {
                minfreq += 1;
            }
        }
        // 插入到 freq + 1 中
        DoublyLinkedList list = freqTable.getOrDefault(freq + 1, new DoublyLinkedList());
        list.addFirst(new Node(key, val, freq + 1));
        freqTable.put(freq + 1, list);
        keyTable.put(key, freqTable.get(freq + 1).getHead());
        return val;
    }
    
    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (!keyTable.containsKey(key)) {
            // 缓存已满，需要进行删除操作
            if (keyTable.size() == capacity) {
                // 通过 minFreq 拿到 freqTable[minFreq] 链表的末尾节点
                Node node = freqTable.get(minfreq).getTail();
                keyTable.remove(node.key);
                freqTable.get(minfreq).remove(node);
                if (freqTable.get(minfreq).size == 0) {
                    freqTable.remove(minfreq);
                }
            }
            DoublyLinkedList list = freqTable.getOrDefault(1, new DoublyLinkedList());
            list.addFirst(new Node(key, value, 1));
            freqTable.put(1, list);
            keyTable.put(key, freqTable.get(1).getHead());
            minfreq = 1;
        } else {
            // 与 get 操作基本一致，除了需要更新缓存的值
            Node node = keyTable.get(key);
            int freq = node.freq;
            freqTable.get(freq).remove(node);
            if (freqTable.get(freq).size == 0) {
                freqTable.remove(freq);
                if (minfreq == freq) {
                    minfreq += 1;
                }
            }
            DoublyLinkedList list = freqTable.getOrDefault(freq + 1, new DoublyLinkedList());
            list.addFirst(new Node(key, value, freq + 1));
            freqTable.put(freq + 1, list);
            keyTable.put(key, freqTable.get(freq + 1).getHead());
        }
    }
}

class Node {
    int key, val, freq;
    Node prev, next;

    Node() {
        this(-1, -1, 0);
    }

    Node(int key, int val, int freq) {
        this.key = key;
        this.val = val;
        this.freq = freq;
    }
}

class DoublyLinkedList {
    Node dummyHead, dummyTail;
    int size;

    DoublyLinkedList() {
        dummyHead = new Node();
        dummyTail = new Node();
        dummyHead.next = dummyTail;
        dummyTail.prev = dummyHead;
        size = 0;
    }

    public void addFirst(Node node) {
        Node prevHead = dummyHead.next;
        node.prev = dummyHead;
        dummyHead.next = node;
        node.next = prevHead;
        prevHead.prev = node;
        size++;
    }

    public void remove(Node node) {
        Node prev = node.prev, next = node.next;
        prev.next = next;
        next.prev = prev;
        size--;
    }

    public Node getHead() {
        return dummyHead.next;
    }

    public Node getTail() {
        return dummyTail.prev;
    }
}
```

- 时间复杂度：get 时间复杂度 $O(1)$ ，put 时间复杂度 $O(1)$ 。由于两个操作从头至尾都只利用了哈希表的插入删除还有链表的插入删除，且它们的时间复杂度均为 $O(1)$ ，所以保证了两个操作的时间复杂度均为 $O(1)$ 。
- 空间复杂度：$O(\textit{capacity})$ ，其中 capacity 为 LFU 的缓存容量。哈希表中不会存放超过缓存容量的键值对。

参考：
- [leetcode题解：LFU](https://leetcode.cn/problems/lfu-cache/solutions/186348/lfuhuan-cun-by-leetcode-solution/)
