# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import namedtuple

class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        Status = collections.namedtuple("Status", ("count", "node"))
        
        def solve(root, p, q):
            if root is None: return Status(0, None)

            left_result = solve(root.left, p, q)
            if left_result.count==2: return left_result

            right_result = solve(root.right, p, q)
            if right_result.count==2: return right_result
        
            matched_nodes = left_result.count+right_result.count+int(root is p)+int(root is q)
            return Status(matched_nodes, root if matched_nodes==2 else None)
        
        return solve(root, p, q).node