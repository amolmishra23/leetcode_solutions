class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def buildGraph(edges):
            graph = defaultdict(list)
            for u,v in edges: graph[u].append(v); graph[v].append(u)
            return graph

        # given a graph and start node. 
        # if we traverse K levels
        # how many nodes are we covering
        def bfs(graph, start, k):
            queue = deque([(start, 0)])
            visited, count = set(), 0

            while queue:
                node, dist = queue.popleft()
                if node in visited or dist>k: continue
                visited.add(node)
                count+=1
                for neigh in graph[node]:
                    queue.append((neigh, dist+1))
            
            return count

        # because its a tree with x edges, we have x+1 nodes exactly
        n, m = len(edges1)+1, len(edges2)+1
        graph1, graph2 = buildGraph(edges1), buildGraph(edges2)
        
        # the 1 edge from graph1 to graph2 is anyways counted
        # rest we can go to k-1 extra levels in graph2. 
        # hence we consider k-1 here. 
        maxGraph2 = max([bfs(graph2, i, k-1) for i in range(m)])
        
        # here we need to compute for each edge in graph1, how far can we traverse
        return [bfs(graph1, i, k)+maxGraph2 for i in range(n)]