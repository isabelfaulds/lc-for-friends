class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        max_length = 0
        l = 0
        for n in range(len(nums)):
            zero_count = zero_count + 1 if nums[n] == 0 else zero_count
            while zero_count > k:
                zero_count = zero_count - 1 if nums[l] == 0 else zero_count
                l += 1
            max_length = max( n - l + 1, max_length )
        return max_length