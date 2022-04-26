class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def solve(node):
            nonlocal ans
            first, second = 0, 0
            for neigh in graph[node]:
                res = solve(neigh)
                if res>first:
                    first, second = res, first
                elif res>second:
                    second = res
            ans = max(ans, first+second)
            return first+1
        
        graph = defaultdict(list)
        
        for s,d in edges:
            graph[s].append(d)
        
        ans = 0
        solve(0)
        return ans