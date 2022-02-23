# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def solve(root):
            if root is None: return 0
            
            left_sum = max(solve(root.left), 0)
            right_sum = max(solve(root.right), 0)
            
            self.global_max = max(self.global_max, left_sum+right_sum+root.val)
            
            return max(left_sum, right_sum)+root.val
        
        self.global_max = float('-inf')
        solve(root)
        return self.global_max