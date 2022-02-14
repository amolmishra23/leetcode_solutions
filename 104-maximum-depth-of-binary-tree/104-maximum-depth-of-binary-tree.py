# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root, curr_level):
            if root is None: return curr_level
            return max(solve(root.left, curr_level+1), solve(root.right, curr_level+1))
        
        return solve(root, 0)