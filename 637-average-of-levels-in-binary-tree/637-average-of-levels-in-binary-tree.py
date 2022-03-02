# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None: return []
        q = deque([root])
        res = []
        while q:
            len_ = len(q)
            temp = []
            for _ in range(len_):
                front = q.popleft()
                temp.append(front.val)
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            res.append(sum(temp)/len(temp))
            
        return res