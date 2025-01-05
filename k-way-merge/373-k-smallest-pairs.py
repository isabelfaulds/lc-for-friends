a  
# 2 ascending sorted integer array
# k smallest pairs , each with 1 from nums1 and 1 from nums2
# min heap or priority queue used to track smallest elements - o n ( len(elements) ) log k (num arrays)

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        # store sum and the indices
        min_heap = []
        
        # initialize a hea
        for i in range( min(k, len(nums1)) ):  # take up to k elements 
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, i, j)
        
        result = []
        
        # use k counter for creation of result
        while k > 0 and min_heap:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # refresh heap with soonest values after current
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        
        return result