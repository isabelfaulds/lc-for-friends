# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# cant use additional data structures
# counting beforehand is fine
# could reverse while sliding across



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        head_counter , n = head , 1
        while head_counter and head_counter.next:
            n += 1
            head_counter = head_counter.next
        group_start = head
        group_end = head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range( n // k ):  # for number of reversals
            group_start = prev.next
            group_end = group_start.next
            # move right the distance of reversal window

            # reverse for the range of reversal window
            for reversal in range(k - 1):
                group_start.next = group_end.next # ie [ 1(group_start),2,3,4,5 ] -> [ 1(group_start),3,4,5 ]
                group_end.next = prev.next # ie [ 2 ... ] & [ (prev) , 1(group_start),3,4,5 ] -> [ 2(group_end),1(group_start),3,4,5 ]
                prev.next = group_end
                group_end = group_start.next
            prev = group_start # prev is at node before next group start

        return dummy.next



# using inspo from lc 92 - reverse between 

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1): # Move prev to node before left
            prev = prev.next
        
        start = prev.next 
        then = start.next
        
        # Reverse the sublist between left and right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next

        