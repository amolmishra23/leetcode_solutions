# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def euler_tour(node, d):
            nonlocal path, depth, p_found, q_found
            
            if p_found and q_found: return 
            if node==p: p_found = True
            if node==q: q_found = True
                
            path.append(node)
            depth.append(d)
            
            if node.left:
                euler_tour(node.left, d+1)
                path.append(node)
                depth.append(d)
                
            if node.right:
                euler_tour(node.right, d+1)
                path.append(node)
                depth.append(d)
                
        path, depth = [], []
        p_found, q_found = False, False
        euler_tour(root, 0)
        
        if not p_found or not q_found: return None
        
        i, j = sorted((path.index(p), path.index(q)))
        
        k = min(range(i, j), key = lambda k: depth[k])
        
        return path[k]