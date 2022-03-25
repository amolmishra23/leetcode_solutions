# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root):
            if not root: return (0, None)
            lh, llca = solve(root.left)
            rh, rlca = solve(root.right)
            if lh > rh: return (lh+1, llca)
            elif rh > lh: return (rh+1, rlca)
            else: return (lh+1, root)
            
        return solve(root)[1]