# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def solve(root, curr_path):
            if root is None: return
            
            curr_path.append(root.val)
            if root.left is None and root.right is None:
                self.res.append("->".join(map(str, curr_path)))
                curr_path.pop()
                return
            
            solve(root.left, curr_path)
            solve(root.right, curr_path)
            curr_path.pop()
            
        self.res = []
        solve(root, [])
        return self.res