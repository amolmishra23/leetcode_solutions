class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Problem is mostly around, making sure we do BFS.
        But dont do continuous loop path 0->1->0->1 again
        To avoid this, we store a seen tuple containing (src,nodes_visited) till then. 
        using this we can avoid it. 
        
        In the end if in any path, we have visited all the nodes, we can return length of path traversal
        """
        n = len(graph)
        goal = (1<<n)-1
        level = [(u, 1<<u) for u in range(n)]
        seen = set(level)
        res = 0
        
        while True:
          nxt = []
          for u, mask in level:
            if mask==goal:
              return res
            for v in graph[u]:
              n_tup = (v, mask | (1<<v))
              if n_tup not in seen:
                nxt.append(n_tup)
                seen.add(n_tup)
          res += 1
          level = nxt
          
        