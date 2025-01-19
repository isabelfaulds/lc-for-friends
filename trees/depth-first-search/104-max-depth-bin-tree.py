# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs - each level first
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        node_queue = deque([root])
        while node_queue:
            level_size = len(node_queue)
            res += 1
            for _ in range(level_size):
                node = node_queue.popleft()
                for child in [node.left,node.right]:
                    if child:
                        node_queue.append(child)
        return res

# dfs - each branch depth first
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)