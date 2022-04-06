# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        q = deque([root])
        curr_level = 0
        
        while q:
            len_ = len(q)
            curr_level += 1
            
            for _ in range(len_):
                front = q.popleft()
                
                if front.left is None and front.right is None: return curr_level
                
                if front.left: q.append(front.left)
                
                if front.right: q.append(front.right)
            
        return curr_level