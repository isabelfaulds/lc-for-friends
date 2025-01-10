# Segment Trees

```

               [0, 3]   (root: sum of the entire array)
              /    \
         [0, 1]      [2, 3]   (sum of subarrays)
        /    \      /    \
   [0] (1)  [1] (2)  [2] (3)  [3] (4)   (leaves: individual elements)
```

- binary tree for storing segments & processing segments
- each node a segment / range of array
- root node is whole array
- leaves nodes are individual indexes
- each intermediary / internal child node is half of parent recursively

### With Trees as Nodes
```python
class SegmentTree:
    def __init__(self, arr: list[int], l: int, r: int):

```

### With Array
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4* self.n) # segment tree is always 4 * size of n
```

### Lazy Trees
- lazy tree propogation performed with hold off array to wait to perform updates until the right time
- without laziness, updates & queries may need whole tree & o n
- with laziness, time can be o log n or o 1

### References
- https://cp-algorithms.com/data_structures/segment_tree.html
- https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
- https://gist.github.com/yonsweng/645ce59fa5308d1b38c67cd7d00b9145li

