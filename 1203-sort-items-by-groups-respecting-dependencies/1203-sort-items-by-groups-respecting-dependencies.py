class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        def get_topo_order(graph, indegree):
            order = []
            stk = [node for node in range(len(graph)) if indegree[node]==0]
            while stk:
                u = stk.pop()
                order.append(u)
                for v in graph[u]:
                    indegree[v]-=1
                    if indegree[v]==0: stk.append(v)
            return order if len(order)==len(graph) else []
        
        for u in range(len(group)):
            if group[u]==-1:
                group[u]=m
                m+=1
        
        items_graph, items_indegree = [[] for _ in range(n)], [0 for _ in range(n)]
        groups_graph, groups_indegree = [[] for _ in range(m)], [0 for _ in range(m)]
        
        for v, before in enumerate(beforeItems):
            for u in before:
                items_graph[u].append(v); items_indegree[v]+=1
                gu, gv = group[u], group[v]
                if gu!=gv:
                    groups_graph[gu].append(gv); groups_indegree[gv]+=1
        
        items_order = get_topo_order(items_graph, items_indegree)
        groups_order = get_topo_order(groups_graph, groups_indegree)
        if not items_order or not groups_order: return []
        
        order_inside_group = [[] for _ in range(m)]
        for u in items_order:
            order_inside_group[group[u]].append(u)
            
        res = []
        for u in groups_order:
            res.extend(order_inside_group[u])
            
        return res
                    