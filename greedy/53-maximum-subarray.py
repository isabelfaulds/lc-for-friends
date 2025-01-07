
# 2 pointer would be o n squared
# kadane's algorithm - start new when its bigger than subarray
# using max
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

### checking if subarray sum is less than just the current index, if true then start fresh
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        a_sum = 0
        for n in nums:
            if a_sum + n < n:
                a_sum = n
            else:
                a_sum += n
            if a_sum > maxsum:
                maxsum = a_sum
        return maxsum