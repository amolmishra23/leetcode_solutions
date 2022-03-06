# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, max_):
        if node is None: return
        
        if node.val >= max_: self.res += 1
        tmp = max(node.val, max_)
        self.preorder(node.left, tmp)
        self.preorder(node.right, tmp)
        
        
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.preorder(root, root.val)
        return self.res