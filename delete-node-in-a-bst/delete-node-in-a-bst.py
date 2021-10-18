# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestNode(self, root):
        """
        Intent is to find the leftmost child in the right sub tree
        """
        if root.left: return self.smallestNode(root.left)
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Find the child node and delete it based on 4 conditions. 
        node doesn't have left or right - return null
        node only has left subtree- return the left subtree
        node only has right subtree- return the right subtree
        node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree
        """
        if root is None: return None
        
        if key<root.val: root.left = self.deleteNode(root.left, key)
        elif key>root.val: root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None: return None
            elif root.left is None: return root.right
            elif root.right is None: return root.left
            else: 
                smallest = self.smallestNode(root.right)
                root.val = smallest.val 
                root.right = self.deleteNode(root.right, smallest.val)
                
        return root