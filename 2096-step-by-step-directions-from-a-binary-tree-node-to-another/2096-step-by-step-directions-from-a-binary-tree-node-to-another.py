# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(root, target, path):
            if root.val == target: return True
            if root.left and find(root.left, target, path):
                path += "L"
                return True
            elif root.right and find(root.right, target, path):
                path += "R"
                return True
            return False
        
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        
        while s and d and s[-1]==d[-1]:
            s.pop()
            d.pop()
            
        return "".join("U"*len(s)) + "".join(reversed(d))
        