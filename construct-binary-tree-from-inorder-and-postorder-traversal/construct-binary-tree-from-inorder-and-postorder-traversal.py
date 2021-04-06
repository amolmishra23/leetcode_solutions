# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(start, end):
            if start>end: return None
            
            temp = postorder[self.post_index]
            new_node = TreeNode(temp)
            self.post_index-=1
            
            new_node.right = build(map_[temp]+1, end)
            new_node.left = build(start, map_[temp]-1)
            
            return new_node
        
        self.post_index = len(postorder)-1
        map_={}
        for i, elem in enumerate(inorder):
            map_[elem]=i
        
        return build(0, len(postorder)-1)