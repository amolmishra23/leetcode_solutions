# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        # 0 for left, 1 for right
        def solve(node, direction, steps):
            if node is None: return 0
            self.res = max(self.res, steps)
            
            if direction==0:
                solve(node.left, 1, steps+1)
                solve(node.right, 0, 1)
            else:
                solve(node.right, 0, steps+1)
                solve(node.left, 1, 1)
        
        solve(root, 0, 0); solve(root, 0, 0); return self.res