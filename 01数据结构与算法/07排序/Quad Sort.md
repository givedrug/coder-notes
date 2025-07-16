# Quad Sort


Quad排序是一种优化版的归并排序，同时也是一个稳定的排序算法，由Igor van den Hoven于2020年提出。Quad排序在多项基准测试中超过Tim排序和内省排序。同时由其衍生出多种排序算法，包括Blitsort, Crumsort, Fluxsort, Gridsort, Twinsort, Piposort, Wolfsort, Robin Hood Sort等。

Quad排序的核心思想是Quad swap（四元交换），即一次对四个元素进行排序，之后在对已排序的序列进行归并处理，直到所有元素有序。

传统做法中，交换2个元素时，借助了第1个临时变量：

```java
if (val[0] > val[1]) {
    tmp[0] = val[0];
    val[0] = val[1];
    val[1] = tmp[0];
}
```

Quad swap是借助4个临时变量，来对4个元素做排序：

```java
// 首先使得tmp[0]<=tmp[1]，tmp[2]<=tmp[3]
if (val[0] > val[1]) {
    tmp[0] = val[1];
    tmp[1] = val[0];
} else {
    tmp[0] = val[0];
    tmp[1] = val[1];
}
if (val[2] > val[3]) {
    tmp[2] = val[3];
    tmp[3] = val[2];
} else {
    tmp[2] = val[2];
    tmp[3] = val[3];
}
// 如果tmp[0]，tmp[1]整体小于tmp[2]，tmp[3]或者反过来，则直接排序完成
if (tmp[1] <= tmp[2]) {
    val[0] = tmp[0];
    val[1] = tmp[1];
    val[2] = tmp[2];
    val[3] = tmp[3];
} else if (tmp[0] > tmp[3]) {
    val[0] = tmp[2];
    val[1] = tmp[3];
    val[2] = tmp[0];
    val[3] = tmp[1];
} else {
	// 对于其他情况，则可以分别对tmp[0]与tmp[2]进行排序，以及tmp[1]与tmp[3]进行排序
    if (tmp[0] <= tmp[2]) {
        val[0] = tmp[0];
        val[1] = tmp[2];
    } else {
        val[0] = tmp[2];
        val[1] = tmp[0];
    }
    if (tmp[1] <= tmp[3]) {
        val[2] = tmp[1];
        val[3] = tmp[3];
    } else {
        val[2] = tmp[3];
        val[3] = tmp[1];
    }
}
```

Quad排序在最优情况下的时间复杂度为$O(n)$，最差情况下的时间复杂度为$O(n \log n)$，期望时间复杂度为$O(n \log n)$。Quad排序的空间复杂度为$O(n)$。

参考： [quadsort](https://github.com/scandum/quadsort)
