# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if node is None: return
        self.inorder(node.left)
        self.res = min(self.res, abs(node.val-self.prev))
        self.prev = node.val
        self.inorder(node.right)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res, self.prev = float('inf'), float('inf')
        self.inorder(root)
        return self.res
        
        