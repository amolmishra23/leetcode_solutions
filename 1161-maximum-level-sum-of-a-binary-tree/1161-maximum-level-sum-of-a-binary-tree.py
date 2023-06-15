# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level_sum, level):
            if not node: return
            
            if len(level_sum)==level:
                level_sum.append(node.val)
            else:
                level_sum[level]+=node.val
            
            dfs(node.left, level_sum, level+1)
            dfs(node.right, level_sum, level+1)
        
        level_sum = []
        dfs(root, level_sum, 0)
        return 1+level_sum.index(max(level_sum))