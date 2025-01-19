# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        res = []
        while node_queue: # on the level
            level_size = len(node_queue)
            level = []
            for _ in range(level_size):
                node = node_queue.popleft()
                level.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        node_queue.append(child)
            res.append(level)
        return res
