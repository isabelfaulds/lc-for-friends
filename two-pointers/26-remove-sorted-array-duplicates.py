# tracker_pointer - moves when a unique int is found
# current_pointer - always moves
# 2 pointer - fast and slow pointer

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker_pointer = 0
        current_pointer = 1

        if len(nums) <= 1:
            return len(nums)

        while current_pointer < len(nums) :
            if nums[current_pointer] == nums[tracker_pointer]:
                current_pointer += 1
                continue
            
            if nums[current_pointer] != nums[tracker_pointer] and current_pointer - tracker_pointer > 1:
                tracker_pointer += 1
                nums[tracker_pointer] = nums[current_pointer]
                continue

            if nums[current_pointer] != nums[tracker_pointer] and current_pointer - tracker_pointer == 1:
                current_pointer += 1
                tracker_pointer += 1


        nums = nums[:tracker_pointer + 1]
        return tracker_pointer + 1

# More Concise
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker_pointer, current_pointer = 0 , 1
        if len(nums) <= 1:
            return len(nums)
        
        while current_pointer < len(nums):
            if nums[current_pointer] != nums[tracker_pointer]:
                tracker_pointer += 1
                nums[tracker_pointer] = nums[current_pointer]
            
            current_pointer += 1

        # The number of unique elements is tracker_pointer + 1
        return tracker_pointer + 1
