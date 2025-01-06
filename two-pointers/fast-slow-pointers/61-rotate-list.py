# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




# optimizing first attempt
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case for no changes
        if not head or not head.next:
            return head
        hare , list_length = head , 1
        
        # counting the length to see how much rotation is needed
        while hare and hare.next:
            hare = hare.next
            list_length += 1
        k = k % list_length # manipulate k directly
        if k == 0:
            return head

        tortoise = head
        # use step range instead of while
        for _ in range(list_length - k - 1):
            tortoise = tortoise.next
        # grab the new head
        new_head = tortoise.next
        # break the list where the new head starts
        tortoise.next = None
        # connect the old tail to the old head
        hare.next = head #last segment of new_head points to old head

        return new_head


# notes
# rotate - shift elements of the linked list by k positions , wrapping around the end of the list
# if k > len(head) / list n , rotation is k%n , continues wrapping

# identify end of list
# end of list . next = head
     # only need to connect the last node to the head once to form circular list
# first attempt
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case for no changes
        if head == None or head.next == None:
            return head
        hare , hare_i = head , 0
        tortoise , tortoise_i = head , 0
        # making a dummy head 
        dummy = ListNode(0)
        
        # counting the length to see how much rotation is needed
        while hare and hare.next:
            hare = hare.next
            hare_i += 1
        rotation_length = k % i # disregarded - k // i full rotations
        if rotation_length == 0:
            return head
        # key index for the node before the new head
        rotation_start = i - rotation_length - 1
        while tortoise_i < rotation_start - 1: # go to before the node
            tortoise = tortoise.next
            tortoise_i += 1
        # grab the node for start of rotation
        new_head = tortoise.next
        # cut off the end of the list
        tortoise.next = None
        dummy.next = new_head
        while new_head:
            if not new_head.next:
                new_head.next = head
                break
            new_head = new_head.next
        return dummy.next

