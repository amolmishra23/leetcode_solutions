class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stopToRoute = collections.defaultdict(set)
        
        # make a map of at particular stop, what all buses pass through
        # idea is, when we traverse a particular stop, we iterate all passing buses, and all routes possible through those buses
        # and finally check which is the minimum most level, at which, we reach destination
        for i, stops in enumerate(routes):
            for stop in stops: 
                stopToRoute[stop].add(i)
                
        bfs = [(S,0)]
        # visited for both bus and stops, to not repeat again
        seenStops = {S}
        seenRoutes = set()
        
        for stop, count in bfs:
            if stop == T: 
                return count
            
            for routeIndex in stopToRoute[stop]:
                if routeIndex not in seenRoutes:
                    seenRoutes.add(routeIndex)
                    for next_stop in routes[routeIndex]:
                        if next_stop not in seenStops:
                            seenStops.add(next_stop)
                            bfs.append((next_stop, count+1))
        
        return -1