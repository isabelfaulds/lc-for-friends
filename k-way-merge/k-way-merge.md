- ✅ already sorted arrays

#### Use Cases
- sort chunks of data in memory without accessing all

#### Data Structures
- heaps / priority queues : top min element will always be accessible in o log k
- merging lists o ( n * k * log k ) - k : num lists , n : avg(len(list))
- extracting smallest - o log k 
- inserting element - o log k


```python
import heapq
heapq.heappush(min_heap, (nums[i] , nums2[0] ))
heapq.heappop(min_heap)
```

