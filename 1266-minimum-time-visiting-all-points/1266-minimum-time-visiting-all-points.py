class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        
        for i in range(1, len(points)):
            prev, curr = points[i-1:i+1]
            res += max(abs(prev[0]-curr[0]), abs(prev[1]-curr[1]))
        
        return res