# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @functools.lru_cache(None)
        def solve(node, parent_chosen):
            if node is None: return 0
            # Same logic to solve like the house robber problem
            # where we need to choose in alternate sequence.
            # just need to make sure if parent was chosen or not
            
            if parent_chosen:
                # parent node was used.
                # we cannot use the child node
                # directly return skipping the child node. 
                return solve(node.left, False) + solve(node.right, False)
            else:
                # parent node is not used
                # we can either choose this node, or not choose this node. 
                # we see which of those options gives us a better answer, and return accordingly. 
                return max(
                    node.val + solve(node.left,True) + solve(node.right, True),
                    solve(node.left, False) + solve(node.right, False)
                )
            
        return solve(root, False)