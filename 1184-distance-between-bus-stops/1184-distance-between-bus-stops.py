class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """
        Very basic question.
        As its 1d array, we need to find minimum of either source to destination or destination to source
        """
        
        if start>destination: start, destination = destination, start
        s_to_d = sum(distance[start:destination])
        d_to_s = sum(distance[0:start]+distance[destination:len(distance)])
        
        print (s_to_d, d_to_s)
        return min(s_to_d, d_to_s)