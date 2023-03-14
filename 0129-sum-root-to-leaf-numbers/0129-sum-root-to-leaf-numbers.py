# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(node, curr):
            if node is None: return
            if node.left is None and node.right is None: curr=curr*10+node.val; self.res+=curr; return
            curr = curr*10+node.val
            solve(node.left, curr)
            solve(node.right, curr)
            
        self.res = 0; solve(root, 0); return self.res