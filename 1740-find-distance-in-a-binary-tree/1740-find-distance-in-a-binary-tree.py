# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, node: Optional[TreeNode], p: int, q: int) -> int:
        def find_lca(root):
            if root is None: return root
            if root.val in {p, q}: return root
            
            left, right = find_lca(root.left), find_lca(root.right)
            
            if left and right: return root
            
            return left or right
        
        def distance(node, target):
            if node is None: return float("inf")
            
            if node.val==target: return 0
            
            return 1+min(distance(node.left, target), distance(node.right, target))
        
        lca = find_lca(node)
        return distance(lca, p)+distance(lca, q)