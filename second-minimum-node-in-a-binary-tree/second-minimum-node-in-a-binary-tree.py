# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node):
        """
        Whole idea is, parent node is equal of smaller than child node.
        Only need is to find the next bigger node, after the root node. 
        if we found node smaller than root, store it in self.res
        if we are still traversing node==root.val, we have need to traverse node.left and node.right.
        in the end also, if no node is left, we just return -1
        """
        if node is None: return
        
        if self.min1<node.val<self.res:
            self.res = node.val
        elif node.val == self.min1:
            self.preorder(node.left)
            self.preorder(node.right)
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min1, self.res = root.val, float('inf')
        self.preorder(root)
        return self.res if self.res!=float('inf') else -1