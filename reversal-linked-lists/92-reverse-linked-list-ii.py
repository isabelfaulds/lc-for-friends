# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # set a dummy to hold for edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1): # Move prev to node before left
            prev = prev.next
        
        start = prev.next 
        then = start.next
        
        # Reverse in between left and right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next