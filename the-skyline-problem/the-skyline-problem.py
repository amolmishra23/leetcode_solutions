from heapq import heappop, heappush

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Reason of putting in this weird way is
        First pref is obviously to sort using L
        
        If L's clash, one with bigger height needs to be processed first. (So that we can ignore one with smaller height)

        And if both L and H clash, we should go first for smaller R(processing the finish events first). 
        Then going with new start events
        So as to remove the entry first
        """
        
        # all the start events
        events = [(L, -H, R) for L, R, H in buildings]
        # all the end events
        events += list({(R, 0, 0) for _, R, _ in buildings})
        # sorting based on the conditions specified above
        events.sort()
        
        # res is the result of important events to get borders
        # live is the currently processing events/maxheap per se
        res, live = [[0, 0]], [(0, float('inf'))]
        
        for pos, negH, R in events:
            # popping buildings that are already ended. 
            # if live[0][1] (end of prev building) is same as the current building start, meaning its ending event
            while live[0][1] <= pos: heappop(live)
                
            # if this building has a height(its a starting building), push it to heap. (height and ending)
            if negH: heappush(live, (negH, R))
                
            # the idea here being, if current highest height is not same as res last height
            # something drop popped in line 21, and hence we got to push a new event with curr max height
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
                
        return res[1:]
                
        
        