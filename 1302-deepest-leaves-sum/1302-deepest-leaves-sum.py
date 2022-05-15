# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q, res = deque([root]), 0
        
        while q:
            res = 0
            for _ in range(len(q)):
                curr = q.popleft()
                res += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                    
        return res