# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [5,4,7,3,null,2,null,-1,null,9] is how leetcode does it
# binary search tree has unique property
    # left subtree contains values smaller than the root
    # right subtree has values larger than the root
    # preorder traversal - root , left , right
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(node):
            nonlocal res
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(map(str, res))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return []
        vals = collections.deque(int(val) for val in data.split(','))
        prev = float('inf')
            # 2 : place
            # 1 : place downstairs of 2
            # 3 : > previous , place right of 1
                # need to see if within range
        def dfs(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = dfs(min_val, val)
                node.right = dfs(val, max_val)
                return node

        return dfs( float('-inf') , float('inf')) 

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans