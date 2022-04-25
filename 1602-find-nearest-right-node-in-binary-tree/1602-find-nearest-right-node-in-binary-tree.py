# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque([(root, 0)])
        
        while q:
            curr, level = q.popleft()
            if curr == u:
                if q and q[0][1] == level: return q[0][0]
                return None
            if curr.left: q.append((curr.left, level+1))
            if curr.right: q.append((curr.right, level+1))
                
        return None
