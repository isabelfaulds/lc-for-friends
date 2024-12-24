# o of n solution

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        counter = 0
        start = 0
        for i, n in enumerate(nums):
            print(i, start, n)
            counter += nums[i]

            while counter >= target:
                # print('range' , i - start + 1)
                if i - start + 1 < min_length:
                    min_length = i - start + 1
                
                counter -= nums[start]
                start += 1
        min_length = 0 if min_length == float('inf') else min_length
        return min_length                        

            
# o log n solution
