# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def solve(node):
            if node is None: return 0
            
            left_val = solve(node.left)
            if left_val!=0: return left_val
            
            self.k -= 1
            if self.k==0: return node.val
            
            right_val = solve(node.right)
            return right_val
        
        self.k = k
        return solve(root)