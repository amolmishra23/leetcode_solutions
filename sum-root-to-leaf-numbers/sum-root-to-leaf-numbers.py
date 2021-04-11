# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def solve(root, curr):
            if root:
                if root.left is None and root.right is None:
                    self.res += curr*10+root.val
                    return 

                solve(root.left, curr*10+root.val)
                solve(root.right, curr*10+root.val)

        self.res = 0
        solve(root, 0)
        return self.res