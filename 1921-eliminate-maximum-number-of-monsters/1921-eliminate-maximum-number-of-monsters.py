class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i, time in enumerate(sorted([d/s for d, s in zip(dist, speed)])):
            if time<=i: return i
            
        return len(dist)