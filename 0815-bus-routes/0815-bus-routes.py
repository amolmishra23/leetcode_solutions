class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Whole idea is, have a 2 way map
        starting from source stop 
        (we need to find all the stops we can reach from all buses from source stop)
        like this every bus change we keep adding it as 1 extra curr_dist
        """
        bus_to_stop = routes
        stop_to_bus = defaultdict(list)
        
        for bus, route in enumerate(bus_to_stop):
            for stop in route:
                stop_to_bus[stop].append(bus)
                
        queue = deque([(source, 0)])
        visited_bus, visited_stop = set(), set()
        
        while queue:
            curr_stop, curr_dist = queue.popleft()
            if curr_stop==target: return curr_dist
            
            for bus in stop_to_bus[curr_stop]:
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    for new_stop in bus_to_stop[bus]:
                        if new_stop not in visited_stop:
                            visited_stop.add(new_stop)
                            queue.append((new_stop, curr_dist+1))
                            
        return -1
            
        