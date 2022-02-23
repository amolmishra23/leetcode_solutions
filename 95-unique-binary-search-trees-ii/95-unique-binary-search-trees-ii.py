# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(first, last):
          
          res = [] 
          
          for root in range(first, last+1):
            for left in solve(first, root-1):
              for right in solve(root+1, last):
                node = TreeNode(root)
                node.left = left
                node.right = right
                res.append(node)
                
          return res or [None]
        
        return solve(1, n)