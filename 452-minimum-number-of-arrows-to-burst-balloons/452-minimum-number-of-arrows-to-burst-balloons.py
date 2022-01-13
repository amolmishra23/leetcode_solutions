class Solution:
    """
    This looks similar to the meeting rooms problem. 
    We need to keep finding which is the minimum j in colling (i,j) points, and shoot a common arrow through j
    As many common arrows we found, that is basically our result. 
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        # sorting so as to find the common points. 
        points.sort(key = lambda x:x[0])
        res, i = 0, 0
        
        while i<len(points):
            # finding the points j coordinate, to find how many common clashing points we find. 
            right_bound = points[i][1]
            j=i+1

            # iterating across the points. 
            while j<len(points) and points[j][0] <= right_bound:
                right_bound = min(right_bound, points[j][1])
                j+=1
            
            # incrementing res
            res += 1
            i=j

        return res