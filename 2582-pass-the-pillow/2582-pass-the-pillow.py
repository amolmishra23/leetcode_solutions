class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        if we have n people, we need n-1 to completely traverse once. 
        """
        if time<n:
            return time+1
        
        each_iteration, dirr = n-1, 0
        while time>n-1:
            time-=(n-1)
            dirr ^= 1
        
        if dirr==1: return n-time
        return time+1
        