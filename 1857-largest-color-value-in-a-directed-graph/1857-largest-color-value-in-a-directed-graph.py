class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # colors length is number of nodes. 
        # colors[i] is color at node[i]
        graph, count = defaultdict(list), [[0]*26 for _ in range(len(colors))]
        indegree = defaultdict(int)
        
        # creating topological sorts DS's
        for x, y in edges:
            graph[x].append(y); indegree[y] += 1
        
        # finding the nodes with 0 indegree to start 
        queue, visited_count, res = deque(), 0, 0
        for x in range(len(colors)):
            if indegree[x]==0: queue.append(x)
        
        while queue:
            for _ in range(len(queue)):
                # if we extracted from queue, its surely only when indegree count was 0
                # meaning no cycles/cyclic dependency. a=>b=>c=>a means a will definitely have indegree 1 always
                # So can consider it for calculating number of visited nodes
                visited_count += 1
                curr_node = queue.popleft()
                curr_color = ord(colors[curr_node])-ord("a")
                # adding count of current color
                count[curr_node][curr_color]+=1
                # updating res
                res = max(res, count[curr_node][curr_color])
                
                # updating current node color, and previous colors to all child nodes. 
                for neigh in graph[curr_node]:
                    # iterate all the colours
                    for c in range(26):
                        count[neigh][c] = max(count[neigh][c], count[curr_node][c])
                    indegree[neigh]-=1
                    if indegree[neigh]==0: queue.append(neigh)

        # if we didnt hit cycle, return res
        return res if visited_count==len(colors) else -1
                    