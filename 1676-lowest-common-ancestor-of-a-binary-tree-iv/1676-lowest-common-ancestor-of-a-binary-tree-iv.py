# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def solve(root):
            if root is None or root in nodes: return root
            
            left, right = solve(root.left), solve(root.right)
            
            if left and right: return root
            
            return left or right
        
        return solve(root)