class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        self.sum = sum(batteries)
        
        while batteries[-1]>self.sum//n:
            n -= 1
            self.sum -= batteries.pop()
            
        return self.sum//n