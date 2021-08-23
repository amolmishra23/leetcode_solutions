# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def preorder(root):
            if root is None: return False
            
            if k-root.val in self.visited: return True
            
            self.visited.add(root.val)
            
            return preorder(root.left) or preorder(root.right)
        
        self.visited = set()
        return preorder(root)