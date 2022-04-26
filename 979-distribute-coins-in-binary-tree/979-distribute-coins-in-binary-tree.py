# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def postorder(root):
            if root is None: return 0
            
            nonlocal moves
            
            left, right = postorder(root.left), postorder(root.right)
            moves += abs(left)+abs(right)
            return root.val + left + right - 1
        
        postorder(root)
        return moves