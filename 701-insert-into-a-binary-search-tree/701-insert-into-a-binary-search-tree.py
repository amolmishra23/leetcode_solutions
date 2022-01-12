# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # in the end of the traversal, we create the node
        if root==None: return TreeNode(val)
        # else we keep traversing passing left and right
        # and keep re-substituting them again
        if root.val < val: root.right = self.insertIntoBST(root.right, val)
        else: root.left = self.insertIntoBST(root.left, val)
        # finally return the same root node. 
        return (root)
        