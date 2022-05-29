class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        in_degree = [0]*n
        for src, dst in roads: in_degree[src]+=1; in_degree[dst]+=1
        return sum((idx+1)*node for idx, node in enumerate(sorted(in_degree)))