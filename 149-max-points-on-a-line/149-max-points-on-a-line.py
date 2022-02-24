class Solution:
    """
    Just need to do in O(n**2) way
    Every point, we see how many points share a common slope with it.
    Result is max number of points, which shared a maximum slope with it. 
    """
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        
        for i, start in enumerate(points):
            slope_count, same = defaultdict(int), 1
            
            for j in range(i+1, len(points)):
                end = points[j]
                
                if start[0]==end[0] and start[1]==end[1]: same+=1
                else:
                    slope = float('inf')
                    if start[0]-end[0]!=0:
                        slope = (start[1]-end[1])*1.0/(start[0]-end[0])
                    slope_count[slope]+=1
                
            current_max = same
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope]+same)
            
            max_points = max(max_points, current_max)
            
        return max_points 
                    