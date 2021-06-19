class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Using a heap data structure below, to effectively get the fuel station providing max fuel most effectively. 
        """
        # we can only reach maximum, as much fuel we have. Lets say 10. 
        max_reachable = startFuel
        heap_ = []
        
        count, index = 0, 0
        
        # until we reached the max
        while max_reachable < target:
            # traverse other stations on the way, until max_reachable, but dont add them as a count as of now.
            # we will store them in a heap
            # if needed, we will use those in future. (giving us maximum fuel)
            
            # quit when you cant go any further
            while index<len(stations) and stations[index][0]<=max_reachable:
                heapq.heappush(heap_, -stations[index][1])
                index += 1
                
            # We are inside the loop, because we didnt reach target. As no more fuel available can return -1
            if not heap_: return -1
            
            max_reachable += -heapq.heappop(heap_)
            count+=1
            
        return count
            