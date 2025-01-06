# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# linked list reversal pattern

# the list is 0 , n , 1 , n - 1 , 2 , n - 2
 # 2 alternating patterns - increasing from start and decreasing from end
 # treating the 2 segments separately before merging more common
 # 1st pattern is already within the list
 # 2nd pattern is half of the list reversed

 # returns head
 # allowed to break list into segments
 # reverse a segment
 # relink nodes to create a single segment
 # in place - dont create a second data structure but indexes within data structure can change

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow_p = head
        fast_p = head
        h1 = head

        # get to middle
        # head.next wont be attempted if first condition fails
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            
        # slow_p in middle, fast_p at end - not a good place to start reversal
        
        h2, curr = None, slow_p.next
        # the list has to be broken off
        slow_p.next = None 
        # list is split before reversing
        while curr:
            next_node = curr.next
            curr.next = h2
            h2 = curr
            curr = next_node

        while h2:
            h1_next , h2_next = h1.next , h2.next

            h1.next = h2
            h2.next = h1_next

            h1 , h2 = h1_next , h2_next