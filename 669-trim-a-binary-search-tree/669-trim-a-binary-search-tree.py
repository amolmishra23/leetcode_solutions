# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        If by change the root.val is not in range of low to high, we trim it off, and just send the left part.
        If at all root.val is in limits, recurse separately on the left and right subtrees. 
        """
        if not root: return None
        
        # these 2 conditions are basically for performing pruning
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # if the curr node is in limit, we recurse on the left and right sub-trees to delete if any nodes not in the range
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root