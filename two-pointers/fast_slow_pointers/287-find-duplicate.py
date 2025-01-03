# o n space like hashmap & frequency array not allowed
# o 1 space single variables allowed
# o n complexity possible

# failed late in test cases due to time constraints , didnt notice this - where each integer is in the range [1, n] inclusive
# the array values should be used for indices for searching without operations needed
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1

        while nums[slow] != nums[fast] and slow != fast:
            # print('starting' , fast , slow)

            fast = ( fast + 2 ) % len(nums)
            slow = ( slow + 1 ) % len(nums)
            # print('added', fast , slow)
            if slow == fast:
                fast = ( fast + 1 ) % len(nums)

            # if nums[slow] == nums[fast] and slow != fast:
                # print(nums[slow], nums[fast], 'found')
        return nums[fast]

# no initial offset in slow fast pointer and using indice values for traversing
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:

            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
