class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_graph(edges):
            graph = defaultdict(list)
            for u,v in edges:
                graph[u].append(v); graph[v].append(u)
            return graph

        def dfs(graph, node, parent, depth, parity, color):
            parity[depth%2] += 1; color[node]=(depth%2)
            for neigh in graph[node]:
                if neigh!=parent:
                    dfs(graph, neigh, node, depth+1, parity, color)

        graph1, graph2 = build_graph(edges1), build_graph(edges2)
        parity1, parity2 = [0,0], [0,0]
        color1, color2 = [-1]*len(graph1), [-1]*len(graph2)
        dfs(graph1, 0, -1, 0, parity1, color1)
        dfs(graph2, 0, -1, 0, parity2, color2)

        parity2_max = max(parity2)
        return [parity2_max + parity1[color1[i]] for i in range(len(graph1))]
