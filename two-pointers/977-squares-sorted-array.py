# Based on x**2 squaring function
# On a number line this function creates a V shape from -inf to +inf
# On a number line large values are at the end, so comparison for sorting would be on opposite ends
# for an arbitrary sorted array there could be negatives so use opposite pointers
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sp = 0 # start pointer
        ep = len(nums) - 1 # end pointer
        new_array = [0] * len(nums)

        for i in range(len(nums) - 1, -1 , -1):
            if nums[ep]**2 >= nums[sp]**2:
                new_array[i] = nums[ep]**2
                ep -= 1
            
            else:
                new_array[i] = nums[sp]**2
                sp += 1
        
        return new_array

