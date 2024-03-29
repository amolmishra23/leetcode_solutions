# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def solve(root, res):
            if root is None: return
            res.append(root.val)
            solve(root.left, res)
            solve(root.right, res)
            
        res = []
        solve(root, res)
        return res