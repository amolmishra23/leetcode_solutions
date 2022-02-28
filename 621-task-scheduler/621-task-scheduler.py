from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        res = 0
        
        for k, v in count.items():
            heapq.heappush(heap, (-v, k))
            
        while heap:
            temp = n+1
            q = []
            
            while temp and heap:
                res += 1
                freq, task = heapq.heappop(heap)
                if -freq>1:
                    q.append((freq+1, task))
                temp -= 1
            
            for item in q:
                heapq.heappush(heap, item)
            
            if heap: res += temp
        
        return res