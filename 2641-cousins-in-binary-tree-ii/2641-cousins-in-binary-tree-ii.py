# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals, stk = [], [(root, 0)]
        
        while stk:
            node, i = stk.pop()
            if i==len(vals): vals.append(0)
            vals[i] += node.val
            if node.left: stk.append((node.left, i+1))
            if node.right: stk.append((node.right, i+1))
                
        stk = [(root,0)]
        
        if root: root.val = 0
            
        while stk:
            node, i = stk.pop()
            child_sum = 0
            if node.left: 
                stk.append((node.left, i+1))
                child_sum += node.left.val
            if node.right: 
                stk.append((node.right, i+1))
                child_sum += node.right.val
            
            if node.left: node.left.val = vals[i+1]-child_sum
            if node.right: node.right.val = vals[i+1]-child_sum
            
        return root