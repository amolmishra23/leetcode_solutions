# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, mn, mx):
        if node is None: return mx-mn
        mn = min(mn, node.val)
        mx = max(mx, node.val)
        return max(self.dfs(node.left, mn, mx), self.dfs(node.right, mn, mx))
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)