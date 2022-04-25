# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        bfs = deque([(root, None)])
        seen = set()
        
        while bfs:
            for _ in range(len(bfs)):
                u, p = bfs.popleft()
                seen.add(u)
                
                if u.right:
                    if u.right in seen:
                        if p.left==u:
                            p.left = None
                        else:
                            p.right = None
                            
                    else:
                        bfs.append((u.right, u))
                        
                if u.left:
                    bfs.append((u.left, u))
                    
        return root