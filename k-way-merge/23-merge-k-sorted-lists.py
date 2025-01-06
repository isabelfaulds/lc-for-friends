# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

# heap q ensures partial sorting
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        # initialize min heap so top is always sorted

        for i, alist in enumerate(lists):
            if alist:
                # first val, index of list, linked list
                heapq.heappush(min_heap, (alist.val, i, alist) )

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            # get the smallest element
            val, i, node = heapq.heappop(min_heap)
            # make the current node link to this
            current.next = node
            # continue from it
            current = current.next
            # print('added to dummy current', current)

            # there's more to the node:
            if node.next:
                # print('such node', node)
                heapq.heappush(min_heap, (node.next.val, i, node.next) )

        # print(min_heap)
        # print(dummy)
        return dummy.next