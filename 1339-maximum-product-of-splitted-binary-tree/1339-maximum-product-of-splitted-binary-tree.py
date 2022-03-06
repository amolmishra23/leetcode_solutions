# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:        
        """
        Basically we do 2 iterations here. 
        1st one, find the entire sum of the tree.
        2nd one, whatever is left sum. We subtract it from total sum, and find the product.
        Same also for the right sum.
        Recursively pre-order like this, we should have the max value in self.res, and return the same. 
        """
        self.res = total = 0
        
        def pre_order(root):
            if root is None: return 0
            
            left = pre_order(root.left)
            right = pre_order(root.right)
            
            self.res = max(self.res, left*(total-left), right*(total-right))
            
            return root.val+left+right
        
        total = pre_order(root)
        pre_order(root)
        return self.res%(10**9+7)