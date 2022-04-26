# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None: return None
        
        root.left = self.solve(root.left)
        root.right = self.solve(root.right)
        
        if root.val in self.to_delete:
            if root.left is not None:
                self.remaining.append(root.left)
            if root.right is not None:
                self.remaining.append(root.right)
            return None
        
        return root
    
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.remaining = []
        self.to_delete = set(to_delete)
        
        if root.val not in self.to_delete:
            self.remaining.append(root)
            
        self.solve(root)
        return self.remaining