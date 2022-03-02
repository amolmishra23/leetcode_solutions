# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node):
        if node is None: return 0
        left_sum, right_sum = self.solve(node.left), self.solve(node.right)
        self.res += abs(left_sum-right_sum)
        return node.val+left_sum+right_sum
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        self.res = 0
        self.solve(root)
        return self.res
        