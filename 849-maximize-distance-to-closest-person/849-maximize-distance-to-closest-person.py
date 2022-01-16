class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        closest = [float('inf')]*len(seats)
        last = None
        
        for i in range(len(seats)):
            if seats[i]==1:
                last = i
            if last is not None:
                closest[i] = i-last
                
        last = None
        for i in range(len(seats)-1, -1, -1):
            if seats[i]==1:
                last = i
            if last is not None:
                closest[i] = min(closest[i], last-i)
                
        return max(closest)