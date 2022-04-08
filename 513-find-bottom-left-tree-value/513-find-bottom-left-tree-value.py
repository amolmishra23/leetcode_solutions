# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        
        def solve(root, idx):
            if root is None: return
            if idx==len(res): res.append(root.val)
            solve(root.left, idx+1)
            solve(root.right, idx+1)
            
        if not root: return 0
        solve(root, 0)
        return res[-1]