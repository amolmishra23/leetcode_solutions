# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

result = collections.namedtuple("result", ("count", "min_val", "max_val"))

class Solution:

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.solve(root)
        return self.res
    
    def solve(self, root):
        if not root: return result(0, float('inf'), float('-inf'))
        
        left_res = self.solve(root.left)
        right_res = self.solve(root.right)
        curr_count = float("-inf")
        
        if left_res.max_val < root.val < right_res.min_val:
            curr_count = left_res.count+right_res.count+1
        
        self.res = max(self.res, curr_count)
        
        return result(curr_count, min(left_res.min_val, root.val), max(right_res.max_val, root.val))