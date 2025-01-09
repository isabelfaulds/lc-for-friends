# intervals interval size is inclusive
# return array for each q in queries
# [ q = min( i in intervals if i[0] <= q <= i[1] else -1 )[size] ]
# o n * m - pairwise combinations

# O(n log n) comes from sorting the intervals.
# O(m log n) comes from performing binary search for each query.

# constraints - 
# 1 to 100k len() intervals array
# 1 to 100k len() queries array
# len() 2 intervals
# interval[0] between 1 , 10000000 <= interval[1] between 1 , 1000000
# q in queries between 1 , 10000000
# brute force that checks each query against every interval inefficient
# cant merge, would disrupt size

# binary search could help for locating i
    # would need to be followed by iteration of checking values & not be as efficient for many same point intervals
    # would need intervals to be sorted
    # could also use 2 pointer
# sorting queries could eleminate possibilites from available array from later indices
# can use greedy for smallest interval

# minimum among set of elements -> heaps
# could use min heap
    # store size, left, right
    
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        min_heap = []
        #  sort intervals & queries
        intervals = sorted(intervals) + [(float("inf") , 0)]
        n = len(intervals)
        sorted_queries = sorted((q,i) for i, q in enumerate(queries) )
        result = [-1] * len(sorted_queries)
        n2 = len(queries)

        p_intervals = 0
        for query, p_query in sorted_queries:
            # print(query, p_query)
            while p_intervals < n and intervals[p_intervals][0] <= query:
                start, end = intervals[p_intervals]
                # print(p_query, p_intervals, start, end)

                heapq.heappush(min_heap, (end - start + 1, start, end))
                p_intervals += 1
            
            while min_heap and min_heap[0][2] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[p_query] = min_heap[0][0]  
    
        return result