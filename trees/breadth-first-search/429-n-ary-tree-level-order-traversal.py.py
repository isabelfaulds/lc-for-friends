"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# breadth first search
# can use a deque to handle on both ends
# create a queue and keep appending to it
# could use a queue for multi threaded applications
# otherwise creating a linked list
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        result = []
        # level processed as a group
        while node_queue:
            # print([i.val for i in node_queue])
            level_size = len(node_queue)
            level = []
            # children nodes added to queue in order
            for _ in range(level_size):
                node = node_queue.popleft()
                # print('removing left for processing')
                # print([i.val for i in node_queue])
                level.append(node.val)
                for child in node.children:
                    node_queue.append(child)
                # print('adding node')
                # print([i.val for i in node_queue])

            result.append(level)
        return result
