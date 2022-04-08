# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def backtrack(n):
            if n==0: return []
            
            if n==1: return [TreeNode()]
            
            res = []
            for l in range(n):
                r = n-1-l
                left_tree, right_tree = backtrack(l), backtrack(r)
                
                for t1 in left_tree:
                    for t2 in right_tree:
                        res.append(TreeNode(0, t1, t2))
                        
            return res
        
        return backtrack(n)