class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [-1 for _ in range(n)]
        for u,v in edges: graph[v]=u
        candidates = [i for i,e in enumerate(graph) if e==-1]
        return candidates[0] if len(candidates)==1 else -1
        
            