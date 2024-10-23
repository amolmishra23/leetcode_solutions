# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = deque(); q.append(root)
        
        while q:
            levelSum, buffer = 0, deque(q)
            for _ in range(len(q)):
                curr = q.popleft()
                # buffer.append(curr)
                if curr.left: q.append(curr.left); levelSum += curr.left.val
                if curr.right: q.append(curr.right); levelSum += curr.right.val
                    
            for node in buffer:
                tmp = levelSum
                if node.left: tmp-=node.left.val
                if node.right: tmp-=node.right.val
                if node.left: node.left.val = tmp
                if node.right: node.right.val = tmp
                    
        return root
        