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
            
            res = solve(node.left)
            if res!=0: return res
            
            self.k -= 1
            if self.k==0: return node.val
            
            return solve(node.right)
        
        self.k = k
        return solve(root)