# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Inorder traversal of a BST will find the nodes in ascending order. So just compare the current node to the previous, and if they match, increase the current count of duplicate values by 1. If they don't match, reset the current count to 1. Compare the current count to the max count found so far. If they match, append the current value to the result list. If the current count of duplicates exceeds the max count, create a new result list with just the current value.
"""
class Solution:
    prev = None
    max_count, curr_count = 0, 0
    res = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.res
    
    def inorder(self, node):
        if node is None: return
        self.inorder(node.left)
        self.curr_count = 1 if node.val != self.prev else self.curr_count+1
        
        if self.curr_count == self.max_count:
            self.res.append(node.val)
        elif self.curr_count>self.max_count:
            self.res = [node.val]
            self.max_count = self.curr_count
            
        self.prev = node.val
        self.inorder(node.right)
            
        