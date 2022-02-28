# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def solve(root, target, curr, cache):
            if root is None: return
            
            curr += root.val
            
            if curr == target: self.res += 1
            
            if (curr-target) in cache: self.res += cache[curr-target]
                
            if curr in cache: cache[curr]+=1
            else: cache[curr]=1
            
            solve(root.left, target, curr, cache)
            solve(root.right, target, curr, cache)
            
            cache[curr]-=1
            
        self.res, cache = 0, {}
        solve(root, targetSum, 0, cache)
        return self.res