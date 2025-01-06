
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

# o n log n


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        cumulative = [0] * ( n + 1 )
        cumulative_counter = 0
        for i in range(n):
            cumulative_counter += nums[i]
            cumulative[i + 1] = cumulative_counter
        
        # binary search on each indice
        min_length = float('inf')
        for i in range(len(cumulative)):
            c_target = cumulative[i] + target

            left , right = i , n
            while left <= right:
                mid = ( left + right ) // 2
                if cumulative[mid] < c_target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left < len(cumulative):
                min_length = min(left - i , min_length)

            

        min_length = 0 if min_length == float('inf') else min_length
        return min_length      


