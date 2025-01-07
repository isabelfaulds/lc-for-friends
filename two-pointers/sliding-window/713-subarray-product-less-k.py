# contiguous subarrays - can't use .sort()
# can use 2 pointer for o of n
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return k
        # for contiguous subarray have loop index be right pointer, left be dynamic to avoid recalculations
        # once the subarray is less than k , all subarrays between l and r are valid
        l = 0
        product = 1
        count = 0
        for r in range(len(nums)):
            product *= nums[r]
            # -1 for test cases with none
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            count += (r - l + 1) # - 1 + 1 for test cases with none
        return count
        