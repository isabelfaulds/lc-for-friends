class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)             

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        value = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if value[i] == "#":
                i += 1
                return None

            root = TreeNode(int(value[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()   
