# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inorder gives elements in sorted order
        Inorder reverse gives elements in descending order
        Keep adding sum to global variable, and update every variable to it. 
        Finally return root node of the tree. 
        """
        
        def solve(root):
            if root is None: return 0
            solve(root.right)
            root.val += self.curr_sum
            self.curr_sum = root.val
            solve(root.left)
        
        self.curr_sum = 0
        solve(root)
        return root