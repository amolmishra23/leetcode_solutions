# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, node: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(root):
            if root is None: return
            if root.left: 
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.right.val].append(root.val)
                graph[root.val].append(root.right.val)
            dfs(root.left); dfs(root.right)
        dfs(node)
        
        visited, res=set([start]), 0
        queue = deque([start])
        
        while queue:
            res += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neigh in graph[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
        
        return res-1