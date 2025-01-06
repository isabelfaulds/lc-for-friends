# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_current = head
        slow_current = head

# using both fast_current and fast_current.next handle even and odd lengths 
# fast_current needs to be not none before attempting to access fast_current.next
        while fast_current and fast_current.next:

            fast_current = fast_current.next.next
            slow_current = slow_current.next

        return slow_current



# slow should always be half of i
# first attempt
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        i = 0
        while current:
            next_node = current.next
            i += 1
            current = next_node
        # print(i)
        mid = ( i // 2 ) + 1
        # print(mid)

        slow = head

        while mid > 1 and slow:
            # print(slow.next)
            next_slow = slow.next
            mid -= 1
            slow = next_slow
            # print(mid, slow)

        return slow