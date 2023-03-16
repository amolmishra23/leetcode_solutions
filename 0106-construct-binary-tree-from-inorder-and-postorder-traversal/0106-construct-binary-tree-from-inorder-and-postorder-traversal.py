# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Last element of postorder is root node of the tree
        # So keep making last node as root, and divide the tree into l,r based on inorder traversal. 
        inorder_idx = {num:i for i, num in enumerate(inorder)}
        curr_idx = len(postorder)-1
        
        def build(start, end):
            nonlocal curr_idx
            if start>end: return None
            temp = postorder[curr_idx]; curr_idx -= 1
            right = build(inorder_idx[temp]+1, end)
            left = build(start, inorder_idx[temp]-1)
            root = TreeNode(temp, left, right)
            return root
        
        return build(0, len(postorder)-1)