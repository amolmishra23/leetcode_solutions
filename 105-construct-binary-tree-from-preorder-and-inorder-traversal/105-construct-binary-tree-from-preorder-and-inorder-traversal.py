# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, pre_order, in_order):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pre_order, in_order, start, end, mapping):
            if start>end: return None
            
            curr = pre_order[self.pre_index]
            node = TreeNode(curr)
            self.pre_index += 1
            
            node.left = build(pre_order, in_order, start, mapping[curr]-1, mapping)
            node.right = build(pre_order, in_order, mapping[curr]+1, end, mapping)
            
            return node
            
        self.pre_index = 0
        mapping = {}
        
        for i, e in enumerate(in_order):
            mapping[e] = i
            
        return build(pre_order, in_order, 0, len(pre_order)-1, mapping)