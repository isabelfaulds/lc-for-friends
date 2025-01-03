# also in slow pointer has some reversal
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# first attempt
# identify middle
# reverse second half of the list and compare to first
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        og = head
        slow_pointer = head
        fast_pointer = head

        # get mid
        # dont need to keep the pointer just before to set prev for second half , on both sides of the palindrome is None and only comparing up until the central pointer
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        # print(slow_pointer)
        
        # reverse slow mid 
        prev = None
        while slow_pointer:
            next_slow = slow_pointer.next
            slow_pointer.next = prev
            prev = slow_pointer
            slow_pointer = next_slow

        while prev:
            next_og = og.next
            next_prev = prev.next
            if og.val != prev.val:
                return False
            prev = next_prev
            og = next_og
        return True

