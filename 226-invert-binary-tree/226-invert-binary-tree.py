# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self, root):
        if root is None: return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        
        root.left, root.right = root.right, root.left
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        A very tricky problem
        Here thing is, we need to reverse the left and right sub-tree. After recursively doing it from the bottom up. 
        For doing it the reverse way, we can make use of the post-order traversal
        """
        self.postOrder(root)
        return root