# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, lst):
            if root is None: return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
            
        lst1, lst2 = [], []
        inorder(root1, lst1)
        inorder(root2, lst2)
        
        i1, i2, res = 0, 0, []
        
        while i1<len(lst1) and i2<len(lst2):
            if lst1[i1]<lst2[i2]:
                res += [lst1[i1]]
                i1+=1
            else:
                res+=[lst2[i2]]
                i2+=1
            
        return res + lst1[i1:]+lst2[i2:]