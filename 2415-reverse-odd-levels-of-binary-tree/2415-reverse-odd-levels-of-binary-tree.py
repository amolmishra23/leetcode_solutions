class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2, level):
            
            ### Actually only need to check one node since it is a perfect binary tree, checking two for easy understanding here.
            if not node1 or not node2:
                return
            
            ### When the level is odd, sweep the value for node1 and node2.
            if level % 2 != 0:
                node1.val, node2.val = node2.val, node1.val
            
            ### The key to using dfs is to pass in the left of node1 and right of node2.
            ### And then, pass in the right of node1 and left of node 2.
            ### These two nodes (node1.left and node2.right) or (node1.right and node2.left) are always on the same level and are the left most and right most nodes that have not been visited.
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        
        ### start with level 1, since level 1 only has 2 nodes, just passing in the left and right with level of 1.
        dfs(root.left, root.right, 1)

        return root