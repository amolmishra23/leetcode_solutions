# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if node is None: return 0
        
        lh, rh = self.height(node.left), self.height(node.right)
        diam = lh + rh + 1
        self.res = max(self.res, diam)
        
        return max(lh, rh)+1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.height(root)
        return self.res-1