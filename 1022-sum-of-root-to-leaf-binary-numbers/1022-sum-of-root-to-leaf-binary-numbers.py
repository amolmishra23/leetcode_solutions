# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        We use the prefix sum concept to solve this problem
        if both child are null, we add the curr sum. 
        Every level down we go, we multiply by 2. 
        Similar to how we *10, while creating decimal numbers. 
        """
        def solve(root, curr_sum):
            if root is None:
                return 
            curr_sum = curr_sum + root.val
            
            if root.left is None and root.right is None:
                self.res += curr_sum
                return
            
            solve(root.left, curr_sum*2)
            solve(root.right, curr_sum*2)
            
        self.res = 0
        solve(root, 0)
        return self.res