# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        q = deque([(root, 0)])
        res = 1
        
        while q:
          res = max(res, q[-1][1]-q[0][1]+1)
          l = len(q)
          for _ in range(l):
            node, idx = q.popleft()
            if node.left: q.append((node.left, 2*idx))
            if node.right: q.append((node.right, 2*idx+1))
            
        return res