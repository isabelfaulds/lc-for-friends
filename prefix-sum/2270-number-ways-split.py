# prefix sum array problem
# [10,4,-8,7] 
# 1st half - i + 1 elements
     # ie i = 1 , 2 elements
# 2nd half - n - i - 1
     # 4 - 1 - 1 = 2 elements
# valid:
     # 1st half >= 2nd half
     # index i + 1 exists
        # ie i = 1 , nums[2]
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # 
        left_sum = 0
        right_sum = sum(nums)

        counter = 0
        for index in range(len(nums) - 1):
            # print(index, nums[index])

            left_sum += nums[index]
            right_sum -= nums[index]

            if left_sum >= right_sum:
                counter += 1
            # print('left', left_sum, 'right', right_sum)
        
        return counter
            