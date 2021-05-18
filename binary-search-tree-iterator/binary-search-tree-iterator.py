# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    """
    Instead of recursive in order traversal, we are doing it through a stack.
    Keep on storing the elements in stack, and keep next pointer to be traversed.
    In case of leaf node, if we reach end of the tree, we will automatically use the top element from stack. 
    """
    def __init__(self, root: TreeNode):
        self.root = root
        self.stk = []

    def next(self) -> int:
        while self.root:
            self.stk.append(self.root)
            # going to the left most
            self.root = self.root.left
        
        self.root = self.stk.pop()
        res = self.root.val
        self.root=self.root.right
        return res
        

    def hasNext(self) -> bool:
        return self.stk or self.root


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()