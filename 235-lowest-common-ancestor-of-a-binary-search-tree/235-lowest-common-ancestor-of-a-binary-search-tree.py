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
            
            # if root lies between p and q, we can return root.
            if p<=root.val<=q: return root
            
            # if max of it lies in left of root. We iterate over the left side
            if max(p, q)<=root.val: return solve(root.left, p, q)
            # else we go on the right side. 
            else: return solve(root.right, p, q)

        p, q = sorted([p.val, q.val])
        return solve(root, p, q)
        