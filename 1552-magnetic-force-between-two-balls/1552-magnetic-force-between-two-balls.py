class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(d, m):
            res, curr = 1, position[0]
            
            for i in range(1, n):
                if res >= m: return True
                if position[i]-curr >= d:
                    res += 1
                    curr = position[i]
                    
            return res >= m
        
        lo, hi = 0, position[-1]-position[0]
        while lo<hi:
            mi = hi - (hi-lo)//2
            if count(mi, m):
                lo = mi
            else:
                hi = mi-1
                
        return lo