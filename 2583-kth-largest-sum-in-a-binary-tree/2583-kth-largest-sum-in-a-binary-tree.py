# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        stk = [(root, 0)]
        
        while stk:
            node, i = stk.pop()
            if i==len(vals): vals.append(0)
            vals[i] += node.val
            if node.left: stk.append((node.left, i+1))
            if node.right: stk.append((node.right, i+1))
                
        return sorted(vals, reverse=True)[k-1] if len(vals)>=k else -1
    