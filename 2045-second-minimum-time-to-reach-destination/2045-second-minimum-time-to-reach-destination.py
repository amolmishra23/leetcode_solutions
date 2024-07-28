class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v); graph[v].append(u)
            # time from u->v is time minutes
            # time from v->u is time minutes
            
        q = deque([1])
        curr_time = 0
        res = -1
        visit_times = defaultdict(list)
        
        while q:
            # in a single iteration all nodes in the queue make progress
            for _ in range(len(q)):
                curr_node = q.popleft()
                if curr_node == n:
                    if res != -1: 
                        return curr_time
                    res = curr_time
                    
                for neigh in graph[curr_node]:
                    # this visit of neigh we reached at time == curr_time
                    # only if its the first time visit
                    # or if its second time visit and takes longer than first time visit
                    nei_times = visit_times[neigh]
                    if len(nei_times)==0 or (len(nei_times)==1 and nei_times[0]!=curr_time):
                        visit_times[neigh].append(curr_time)
                        q.append(neigh)
                    
            # if right now we are in the odd cycle, such that we cannot make movement
            # then we make our curr_time reach the nearest even cycle
            if (curr_time//change) % 2 == 1:
                curr_time += change - (curr_time % change)

            # after we are done with the iteration, adding that we took "time" duration
            # in the current iteration
            curr_time += time
            
        