# first attempt single pointer
    # pop() operates in o(1) but involves memory adjustments for shrinking the list
    # use 2nd pointer instead
    # check for m outside of loop
    # can use more descriptive names
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        r = m - 1

        for i in range( m + n -1 , -1 , -1):

            if n == 0:
                break

            if m == 0 or ( nums2[-1] >= nums1[r] ) :
                nums1[i] = nums2.pop(-1)
                n -= 1

            else:
                nums1[i] = nums1[r]
                nums1[r] = 0
                r -= 1
                m -= 1 

# Reverse 2 pointer solution
# Pointers start at end of the arrays and work backwards
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 , p1 = m - 1  , n - 1 # last elements
        p = m + n - 1  # Pointer for the last index in nums1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
