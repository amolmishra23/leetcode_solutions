class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_reachable = startFuel
        heap = []
        
        count, idx = 0, 0
        
        while max_reachable < target:
            while idx<len(stations) and stations[idx][0] <= max_reachable:
                heapq.heappush(heap, -stations[idx][1])
                idx += 1
            if not heap: return -1
            max_reachable += (-heapq.heappop(heap))
            count += 1
            
        return count