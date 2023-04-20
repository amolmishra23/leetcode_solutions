# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        q, res = deque(), 1
        q.append((root, 0))
        
        while q:
            res = max(res, q[-1][1]-q[0][1]+1)
            for _ in range(len(q)):
                curr, idx = q.popleft()
                if curr.left: q.append((curr.left, 2*idx))
                if curr.right: q.append((curr.right, 2*idx+1))
            
        return res
        