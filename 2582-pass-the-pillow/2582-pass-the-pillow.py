class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        Each start to end to go, we need n-1 moves
        if rounds_done is even => we now will start from left to right
        if rounds_done is odd => we will start from right to left
        accordingly calculate and return the result. 
        """
        rounds_done, rem_moves = divmod(time,n-1)
        return n-rem_moves if rounds_done%2 else rem_moves+1
    
    def passThePillow1(self, n: int, time: int) -> int:
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
        