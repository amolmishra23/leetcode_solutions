# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTreesHelper(start, end):
            result = []
            
            for root in range(start, end+1):
                for left in generateTreesHelper(start, root-1):
                    for right in generateTreesHelper(root+1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        result.append(node)
                        
            return result or [None]
        
        return generateTreesHelper(1, n)