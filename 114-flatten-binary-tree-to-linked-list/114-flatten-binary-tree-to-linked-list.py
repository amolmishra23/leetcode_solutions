# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        The logic here is to do a reverse post order traversal.
        traverse to the right most. 
        traverse to the left.
        
        Now set right child as self.prev. left as none. 
        And finally cache the current value as self.prev for future purposes.
        """
        if root is None: return
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root