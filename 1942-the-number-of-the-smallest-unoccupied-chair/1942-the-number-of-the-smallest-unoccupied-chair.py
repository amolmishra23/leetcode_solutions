from sortedcontainers import SortedList
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        seats = list(range(len(times)))
        heapq.heapify(seats)
        
        times = [(st,et,idx) for idx, (st, et) in enumerate(times)]
        
        times.sort(key=lambda x: x[0])
        endtimes = SortedList()
        
        for st,et,idx in times:
            while endtimes and endtimes[0][0]<=st:
                elem = endtimes[0]
                heapq.heappush(seats, elem[1])
                endtimes.discard(elem)
                
            seat = heapq.heappop(seats)
            
            if idx==targetFriend: return seat
            
            endtimes.add((et, seat, idx))
            
        return -1
            