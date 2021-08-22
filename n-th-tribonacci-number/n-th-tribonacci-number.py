class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [None]*(38)
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1
        
        def solve(n):
            if cache[n] is not None: return cache[n]
            
            cache[n] = solve(n-1)+solve(n-2)+solve(n-3)

            return cache[n]
        
        return solve(n)