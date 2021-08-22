class Solution:
    def fib(self, n: int) -> int:
        cache = [None]*(31)
        cache[0] = 0
        cache[1] = 1
        
        def solve(n):
            if cache[n] is not None: return cache[n]
            
            cache[n] = solve(n-1)+solve(n-2)

            return cache[n]
        
        return solve(n)