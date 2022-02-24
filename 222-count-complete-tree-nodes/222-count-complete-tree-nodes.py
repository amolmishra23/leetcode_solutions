# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Find the node, whose left and right sub-trees are same height
        And return the number of nodes. O(logn)
        Else, just go recursively and find the height of such tree. O(n)
        """
        if root is None: return 0
        
        lh, rh = 1, 1
        left, right = root.left, root.right
        
        # finding the left and right height
        while left:
            left = left.left
            lh += 1
        while right:
            right = right.right
            rh += 1
        
        # if heights are same, we dont need to traverse all nodes. Just use the formula and return the nodes. 
        if lh == rh: return (2**lh)-1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        