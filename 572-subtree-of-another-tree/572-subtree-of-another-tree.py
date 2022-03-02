# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def is_equal(s, t):
            if s is None and t is None: return True
            if s is None or t is None: return False
            if s.val==t.val:
                return is_equal(s.left, t.left) and is_equal(s.right, t.right)
            return False
        
        
        if s is None: return False
        elif is_equal(s, t): return True
        else: return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)