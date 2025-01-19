# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def node_check(l, r):
            if not l and not r: 
                return True
            if (not l or not r) or l.val != r.val:
                return False
            return node_check(l.left , r.right) and node_check(l.right , r.left)

        return node_check(root.left, root.right)

# could use deque for iterative - BFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        node_queue = deque([(root.left, root.right)])
        while node_queue:
            l , r = node_queue.popleft()
            if ( l and r ) and l.val == r.val:
                node_queue.append((l.left, r.right))
                node_queue.append((l.right, r.left))
            if not l and not r:
                continue
            if (not l or not r) or l.val != r.val:
                return False

        return True
