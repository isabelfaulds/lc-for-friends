# O n log n

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def binary_search(arr, target):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + (r - l) // 2  # Overflow safe
                if arr[mid] >= target:  # Move even if = to end loop
                    r = mid
                else:
                    l = mid + 1
            return l

        subsequence_length_array = [] # doesnt need to have order preserved throughout the creation process, preserves length
        for i in range( len(nums) ):
            print(i)
            if not subsequence_length_array or subsequence_length_array[-1] < nums[i]:
                subsequence_length_array.append(nums[i])
            else:
                newindex = binary_search(subsequence_length_array, nums[i])
                subsequence_length_array[newindex] = nums[i]
            # print(i, nums[i], subsequence_length_array)

        return len(subsequence_length_array)
    
# O n ^ 2

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)  # dp[i] will store the length of the LIS ending at index i
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
