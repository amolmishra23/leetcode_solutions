# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def solve(root, p, q):
            if root is None: return None

            if root.val in [p.val, q.val]: return root

            left = solve(root.left, p, q)
            right = solve(root.right, p, q)

            if left is not None and right is not None: return root

            return left or right

        return solve(root, p, q)
        