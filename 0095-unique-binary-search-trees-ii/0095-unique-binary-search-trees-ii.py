# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def solve(start, end):
            """
            As we are dealing with BST, we know for sure
            Left side has values less than root
            Right side has values less than root
            Assuming we make 3 as root. Left subtree has 1,2. 
            Right has 4,5,6,7. 
            Hence we design our recursion like that, to get trees for specific numbers
            Accordingly make all the possible trees
            And return the values
            """
            res = []
            
            for root in range(start, end+1):
                for left in solve(start, root-1):
                    for right in solve(root+1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        res.append(node)
                        
            return res or [None]
        
        return solve(1, n)