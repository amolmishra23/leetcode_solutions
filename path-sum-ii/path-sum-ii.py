# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def solve(root, curr_path, curr_sum, res):
            if root is None: return
            
            curr_path.append(root.val)
            
            if root.left is None and root.right is None and targetSum-curr_sum==root.val:
                res.append(list(curr_path))
                
            if root.left: solve(root.left, curr_path, curr_sum+root.val, res)
            if root.right: solve(root.right, curr_path, curr_sum+root.val, res)
            
            curr_path.pop()
            
        res = []
        solve(root, [], 0, res)
        return res