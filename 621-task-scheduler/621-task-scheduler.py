from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        For choosing which task to do, we can put in a counter. 
        And store it in max_heap, which gives tax with max count remaining. 
        If heap doesnt have any more tasks to do in the same stretch, we can have that many empty slots also in between. 
        
        Meanwhile dont add them back instantly to heap, until the time is period. 
        So we could keep storing in a temp list. 
        """
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