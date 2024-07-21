class Solution:
    def buildMatrix(self, k: int, row_conditions: List[List[int]], col_conditions: List[List[int]]) -> List[List[int]]:
        def topo(conditions):
            res = []
            
            def dfs(src, visited, curr_path):
                nonlocal res
                if src in curr_path: return False
                if src in visited: return True

                visited.add(src); curr_path.add(src)
                
                for neigh in graph[src]:
                    if not dfs(neigh, visited, curr_path): return False
                
                res.append(src); curr_path.remove(src)
                return True
            
            graph = defaultdict(list)
            for u,v in conditions:
                graph[u].append(v)
                
            visited, curr_path = set(), set()
            for u in range(1, k+1):
                if not dfs(u, visited, curr_path):
                    return []
                
            return res[::-1]
        
        row_topo = topo(row_conditions)
        col_topo = topo(col_conditions)
        row_topo_idx = {v:k for k,v in enumerate(row_topo)}
        col_topo_idx = {v:k for k,v in enumerate(col_topo)}
        
        if not row_topo or not col_topo: return []
        
        res = [[0]*k for _ in range(k)]
        
        for i in range(1, k+1):
            m, n = row_topo_idx[i], col_topo_idx[i]
            res[m][n] = i
            
        return res