class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([d/s for d, s in zip(dist, speed)])
        
        for i in range(len(dist)):
            # if time[i]>i: continue
            # else: return i
            if time[i]<=i: return i
            
        return len(dist)