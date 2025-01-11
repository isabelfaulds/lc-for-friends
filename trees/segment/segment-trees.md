# Segment Trees

```

               [0, 3]   (root: sum of the entire array)
              /    \
         [0, 1]      [2, 3]   (sum of subarrays)
        /    \      /    \
   [0] (1)  [1] (2)  [2] (3)  [3] (4)   (leaves: individual elements)
```
- binary tree for storing segments & processing segments
- segment tree array length: 4 * n = len ( array )
- height: log n = len ( array )
- each node a segment / range of array
- root node is whole [:] array
- leaf nodes are individual indexes
- each intermediary / internal child node is half of parent recursively, split by mid index
     - left usually preference for odd length splits

### Tree Objects
```python
class SegmentTree:
    def __init__(self, arr: list[int]):
          self.n = len(list)
          ## Tree storage
          # option a - node objects
          self.tree = [Node() for _ in range(4 * n)] # initialized with empty node objects
          # option b - int array
          self.tree = [0] * (4* self.n) # initialized as an empty 
          ## Lazy propogation
          # option a
          self.lazy = 0 # single lazy value reused for entire tree
          # option b
          self.lazy = [0] * (4* self.n) # lazy value for every node
```

### Nodes
- stores the aggregation value or values
- only one func: init for the valubes
```python
class Node:
    def __init__(self, square_sum=0, sum_=0):
        self.square_sum = square_sum
        self.sum = sum_
```

### Lazy Trees
- lazy tree propogation performed with hold off array or value to wait to perform updates until the right time
- without laziness, updates & queries may need whole tree & o n complexity
- with laziness, time can be o log n or o 1




### References
- https://cp-algorithms.com/data_structures/segment_tree.html
- https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
- https://gist.github.com/yonsweng/645ce59fa5308d1b38c67cd7d00b9145li


