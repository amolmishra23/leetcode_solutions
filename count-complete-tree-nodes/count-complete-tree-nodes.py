# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        
        lh, rh = 1,1
        left = root.left
        while left:
            left = left.left
            lh+=1
        right = root.right
        while right:
            right = right.right
            rh+=1
        
        if lh==rh: return (2**lh)-1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)