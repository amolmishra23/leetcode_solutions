class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.lru_cache(None)
        def solve(x):
            if x<=2: return x
            
            return solve(x-1)+solve(x-2)
        
        return solve(n)