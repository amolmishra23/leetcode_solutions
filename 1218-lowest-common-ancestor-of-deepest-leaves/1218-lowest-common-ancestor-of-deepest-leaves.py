# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return (None, 0)

            lnode, lheight = dfs(node.left)
            rnode, rheight = dfs(node.right)

            if lheight == rheight: 
                return node, 1 + lheight
            elif lheight > rheight:
                return lnode, lheight+1
            else:
                return rnode, rheight+1

        node, _ = dfs(root)
        return node