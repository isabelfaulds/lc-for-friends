# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# cleaner, uses offset
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        hare, tortoise = head, head

        # Move hare n steps ahead
        for _ in range(n):
            if hare:
                hare = hare.next
            else:
                return head  # If n is larger than the length of the list, return the original list
        
        # Move both hare and tortoise until hare reaches the end
        while hare:
            hare = hare.next
            tortoise = tortoise.next
        
        # Remove the nth node from the end
        tortoise.next = tortoise.next.next

        return dummy.next

# second attempt same speed
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        hare , tortoise = head , head
        hi , ti , ni = 0 , 0 , (-1 * n)

        # dont move tortoise prematurely
        while hare:
            hare = hare.next
            hi += 1
        ni += hi - 1# gives the index before the removal

        if ni < 0: # index before the removal is before the head, pop off the top
            return head.next
        
        while tortoise and ti != ni:
            tortoise = tortoise.next
            ti += 1
        
        if not tortoise.next:
            return None
        
        tortoise.next = tortoise.next.next
        return dummy.next

# first attempt failed - didnt take into considereation small length lists or large n tests where moving tortoise moves it past n
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        hare , tortoise = head , head
        hi = 0
        ti = 0
        node_i = (-1 * n)
        # always include hare if checking hare.next
        # hare stops at the last one
        while hare and hare.next:
            hare = hare.next.next
            hi += 2
            tortoise = tortoise.next
            ti += 1
        hi = hi + 1 if hare else hi # even numbered lists will end with hare = None
        node_i += hi - 1 # gives the element before the removal

        if hi <= 1:
            return None
        if hi == 2:
            if n == 1:
                head.next = None
                return head
            if n == 2:
                return head.next
        print(hi, node_i)

        while tortoise and ti and ( ti != node_i) :
            print(tortoise)
            tortoise = tortoise.next
            ti += 1
        if tortoise and tortoise.next:
            tortoise.next = tortoise.next.next

        return dummy.next