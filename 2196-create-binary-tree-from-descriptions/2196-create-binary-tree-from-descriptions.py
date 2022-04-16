# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        all_nodes, child_nodes = set(), set()
        
        for p, x, is_left in descriptions:
            nodes[p] = nodes[p] if p in nodes else TreeNode(p)
            nodes[x] = nodes[x] if x in nodes else TreeNode(x)
            
            if is_left:
                nodes[p].left = nodes[x]
            else:
                nodes[p].right = nodes[x]
            
            all_nodes.add(p); all_nodes.add(x)
            child_nodes.add(x)
                
        return nodes[all_nodes.difference(child_nodes).pop()]