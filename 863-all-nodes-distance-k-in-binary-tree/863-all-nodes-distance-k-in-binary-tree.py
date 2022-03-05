# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(root, par=None):
            if root is not None:
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)
                
        dfs(root)
        
        queue = [(target, 0)]
        seen = {target}
        
        while queue:
            if queue[0][1]==K: return [elem.val for elem,_ in queue]

            len_ = len(queue)
            
            for _ in range(len_):
                popped, dis = queue.pop(0)
                for adj in [popped.left, popped.right, popped.par]:
                    if adj and adj not in seen:
                        seen.add(adj)
                        queue.append([adj, dis+1])
                        
        return []
            
            