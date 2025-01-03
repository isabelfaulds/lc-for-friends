# array is circular, last element loops to first , backwards of first is last
# if nums[i] > 0 can move nums[i] steps
# if nums[i] < 0 can move |nums[i]| steps backward

# confirming a loop 
    # if an index is revisted according to movement rules of indexes within the loop
    # if all indexes move in the same direction
    # if its index size > 1




# first attempt with weird is pos variables
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def get_next(index):
            # This function returns the next index considering the circular array.
            return (index + nums[index]) % len(nums)

        def is_pos(index):
            return nums[index] > 0

        for i in range(len(nums)):
            # If nums[i] is zero, we skip it because it doesn't move anywhere.
            if nums[i] == 0:
                continue
            
            # Initialize slow and fast pointers.
            sp, fp = i, get_next(i)
            og_pos = is_pos(sp)
            sp_pos = og_pos
            fp_pos = is_pos(fp)
            fp_pos2 = is_pos(fp)

            # Determine the direction (positive or negative) from the starting point.
            while sp_pos == og_pos and fp_pos == og_pos and fp_pos2 == og_pos:
                if sp == fp:
                    # If the slow and fast pointers meet, we have found a cycle.
                    if sp != get_next(sp):  # Ensure the cycle length is > 1.
                        return True
                    break  # Single index loop, no valid cycle.

                # Move the slow pointer one step and the fast pointer two steps.
                sp = get_next(sp)
                sp_pos = is_pos(sp)

                fp = get_next(fp)
                fp_pos2 = is_pos(fp)
                fp = get_next(fp)
                fp_pos = is_pos(fp)


        return False

# revised, use product > 0 to check if the 2 signs being compared are the same
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def get_next(index):
            return (index + nums[index]) % len(nums)

        for i in range(len(nums)):
            # If nums[i] is zero, we skip it because it doesn't move anywhere.
            if nums[i] == 0:
                continue
            
            # Initialize slow and fast pointers.
            sp, fp = i, get_next(i)
            # Determine the direction (positive or negative) from the starting point.
            while nums[sp] * nums[fp] > 0 and nums[sp] * nums[get_next(fp)] > 0:
                if sp == fp:
                    # If the slow and fast pointers meet, we have found a cycle.
                    if sp != get_next(sp):  # Ensure the cycle length is > 1.
                        return True
                    break  # Single index loop, no valid cycle.

                # Move the slow pointer one step and the fast pointer two steps.
                sp = get_next(sp)
                fp = get_next(get_next(fp))


        return False

# use markers for faster execution
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False  
        def next_index(index: int) -> int:
            return (index + nums[index]) % n

        for i in range(n):
            if nums[i] == 0:
                continue 

            slow, fast = i, next_index(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                if slow == fast:
                    if slow == next_index(slow):  
                        break
                    return True

                slow = next_index(slow)
                fast = next_index(next_index(fast))

            marker = i
            while nums[marker] * nums[next_index(marker)] > 0:
                temp = marker
                marker = next_index(marker)
                nums[temp] = 0 

        return False


# example of memory optimized, no extra space for tracking visited and only a few pointers
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getIndex(index, isPos):
            direction = nums[index] >= 0
            nextIndex = (index + nums[index]) % len(nums)

            if isPos != direction or index == nextIndex:
                return -1
            
            return nextIndex

        for i in range(len(nums)):
            isPos = nums[i] >= 0
            slow, fast = i,i

            while True:
                slow = getIndex(slow, isPos)
                fast = getIndex(fast, isPos)

                if fast != -1:
                    fast = getIndex(fast, isPos)
                
                if fast == -1 or slow == -1:
                    break
                
                if fast == slow:
                    return True

        return False