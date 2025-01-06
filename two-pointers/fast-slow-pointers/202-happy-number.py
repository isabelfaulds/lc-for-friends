# technically optimized version but slower because function is called more frequently leading to slower performance
# array based indexing for retrieval fast, faster than extra computations

class Solution:
    def isHappy(self, n: int) -> bool:
        def check_happy(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow = n
        fast = check_happy(n)

        while fast != 1 and slow != fast:
            slow = check_happy(slow)
            # needs to be offset and faster
            fast = check_happy( check_happy(fast) )

        return fast == 1

# first attempt - maintained an array and initially placed the pointers offset
class Solution:
    def isHappy(self, n: int) -> bool:
        def check_happy(n_int):
            return sum([int(each) ** 2 for each in str(n_int)])
        nums = [n , check_happy(n) ]
        # print(nums)
        p0  , p1 = 0 , 1
        if nums[p0] == 1 or nums[p1] == 1:
            return True
        if nums[p0] == nums[p1]:
            return False

        while nums[p0] != nums[p1]:
            # print(nums[p0], nums[p1])
            if nums[p0] == 1 or nums[p1] == 1:
                return True
            nums.append(check_happy( nums[-1] ) )
            nums.append(check_happy( nums[-1] ) )
            p0 += 1
            p1 += 2
            # print(nums[p0], nums[p1])
        return False
            