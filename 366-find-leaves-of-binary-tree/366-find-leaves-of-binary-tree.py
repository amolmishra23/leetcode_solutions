# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        
        def dfs(node, layer):
            if node is None: return layer
            
            left, right = dfs(node.left, layer), dfs(node.right, layer)
            layer = max(left, right)
            res[layer].append(node.val)
            return layer+1
        
        dfs(root, 0)
        return res.values()