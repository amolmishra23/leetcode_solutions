class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph, n = defaultdict(list), len(colors)
        for u,v in edges: graph[u].append(v)
        count = [[0]*26 for _ in range(n)]
        visited, curr_path = set(), set()

        def dfs(i):
            if i in curr_path: return float("inf")
            if i in visited: return 0
            curr_path.add(i); visited.add(i)

            curr_color = ord(colors[i])-ord("a")
            count[i][curr_color]=1

            for neigh in graph[i]:
                if dfs(neigh) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[i][c] = max(
                        count[i][c],
                        (1 if c==curr_color else 0) + count[neigh][c],
                    )
            curr_path.remove(i)
            return max(count[i])

        n, res = len(colors), 0
        for k in range(n):
            res = max(dfs(k), res)

        return -1 if res==float("inf") else res
