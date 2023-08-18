class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i, j in roads:
            graph[i].append(j); graph[j].append(i)
            
        res = float("-inf")
        for i in range(n-1):
            for j in range(i+1, n):
                curr = len(graph[i]) + len(graph[j]) - (i in graph[j])
                res = max(res, curr)
        
        return res