class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xDepth = -1
        self.yDepth = -2
        self.xParent = None
        self.yParent = None

        def dfs(root, parent, x, y, depth):
            if root is None: return
            if root.val == x:
                self.xParent = parent
                self.xDepth = depth
            elif root.val == y:
                self.yParent = parent
                self.yDepth = depth
            else:
                dfs(root.left, root, x, y, depth+1)
                dfs(root.right, root, x, y, depth+1)

        dfs(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent