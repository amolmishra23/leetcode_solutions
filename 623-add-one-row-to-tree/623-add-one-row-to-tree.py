# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def preorder(node, level):
            if node is None: return
            if level == depth-1:
                l, r = node.left, node.right
                node.left = TreeNode(val, l, None)
                node.right = TreeNode(val, None, r)
                return
            preorder(node.left, level+1)
            preorder(node.right, level+1)
                
        if depth==1: return TreeNode(val, root)
        preorder(root, 1)
        return root
            