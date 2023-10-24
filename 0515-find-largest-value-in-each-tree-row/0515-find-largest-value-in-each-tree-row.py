# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        
        while any(q):
            res.append(max(node.val for node in q if node))
            q = [child for node in q for child in (node.left, node.right) if child]
    
        return res