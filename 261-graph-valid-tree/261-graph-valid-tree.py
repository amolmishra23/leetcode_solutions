class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        # initialize a parent dict where each vertex belongs to itself
        parent = {i: i for i in range(n)}
        
        # find operation
        def find(v):
            if parent[v] != v:
                # use path compression to gain some time 
                parent[v] = find(parent[v])
            return parent[v]

        for edge in edges:
            # for each edge, check if two vertices belongs to one set
            # if yes then a cycle is found
            set1 = find(edge[0])
            set2 = find(edge[1])
            if set1 == set2:
                return False
                
            # union
            parent[set1] = set2

        return True



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # idea is to return true, as soon as we find a cycle. 
        # condition for graph to be tree is, no cycles, and we should have visited all nodes starting from one node. 
        def dfs(node, visited, parent):
            if node in visited: return True
            
            visited.add(node)
            
            for neigh in graph[node]:
                if neigh==parent: continue
                if dfs(neigh, visited, node): return True
            
        graph = defaultdict(list)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = set()
        has_cyle = dfs(0, visited, -1)
        if has_cyle: return False
        
        return len(visited)==n