class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for i in range(n):
            graph[manager[i]].append(i)
            
        def dfs(node):
            ans = 0
            for neigh in graph[node]:
                ans = max(ans, dfs(neigh) + informTime[node])
                
            return ans
        
        return dfs(headID)