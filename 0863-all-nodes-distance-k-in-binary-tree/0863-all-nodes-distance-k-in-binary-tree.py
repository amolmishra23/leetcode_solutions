# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def construct_graph(par, child):
            if par and child:
                graph[par.val].append(child.val)
                graph[child.val].append(par.val)
            if child.left: construct_graph(child, child.left)
            if child.right: construct_graph(child, child.right)
                
        construct_graph(None, root)
        bfs = deque([target.val])
        seen = set(bfs)
        
        for _ in range(k):
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                for neigh in graph[curr]:
                    if neigh not in seen:
                        bfs.append(neigh)
                
            seen |= set(bfs)
            
        return list(bfs)