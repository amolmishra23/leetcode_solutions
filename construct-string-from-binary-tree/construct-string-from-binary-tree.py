# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if root is None: return ""
            
            temp = str(root.val)
            left = preorder(root.left)
            right = preorder(root.right)
            
            if right!="": 
                temp += "(" + left + ")" + "(" + right + ")"
            elif left!="":
                temp += "(" + left + ")"
            
            return temp
          
        return preorder(root)
        