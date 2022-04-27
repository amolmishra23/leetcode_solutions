# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        
        def construct_graph(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left: construct_graph(child, child.left)
            if child.right: construct_graph(child, child.right)
                
        construct_graph(None, root)
        
        bfs = deque([target.val])
        seen = set(bfs)
        
        for _ in range(k):
            tmp = deque()
            
            while bfs:
                curr = bfs.popleft()
                for neigh in graph[curr]:
                    if neigh not in seen:
                        tmp.append(neigh)
                        
            seen |= set(tmp)
            bfs = tmp
            
        return list(bfs)
                