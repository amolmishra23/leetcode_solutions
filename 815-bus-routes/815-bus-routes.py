class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_to_stop = routes
        
        stop_to_bus = defaultdict(list)
        
        for i, route in enumerate(bus_to_stop):
            for stop in route:
                stop_to_bus[stop].append(i)
                
        visited_stops, visited_bus = set(), set()
        
        q = deque([(source, 0)])
        
        while q:
            curr_stop, curr_count = q.popleft()
            
            if curr_stop == target: return curr_count
                
            for bus in stop_to_bus[curr_stop]:
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    for next_stop in bus_to_stop[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append((next_stop, curr_count+1))
                            
        return -1