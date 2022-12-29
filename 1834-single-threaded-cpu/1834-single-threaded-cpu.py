class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = sorted([(a,b,i) for i, (a, b) in enumerate(tasks)])
        curr_time, heap, res = tasks[0][0], [], []
        i = 0
        
        while len(res) < len(tasks):
            while i<len(tasks) and tasks[i][0]<=curr_time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1
            
            if not heap:
                curr_time = tasks[i][0]
            else:
                process_time, idx = heapq.heappop(heap)
                curr_time += process_time
                res.append(idx)
            
        return res