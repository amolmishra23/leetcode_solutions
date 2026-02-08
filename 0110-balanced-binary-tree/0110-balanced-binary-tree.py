# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def solve(root):
            if root is None: return 0, True

            left_height, left_balanced = solve(root.left)
            right_height, right_balanced = solve(root.right)
            
            return max(left_height,right_height)+1, left_balanced and right_balanced and abs(left_height-right_height)<=1
        
        _, is_balanced = solve(root)
        return is_balanced