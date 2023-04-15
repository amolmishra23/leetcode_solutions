class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def solve(i, k):
            if k==0 or i==len(piles): return 0
            
            res, curr_sum = solve(i+1, k), 0
            
            for j in range(min(k, len(piles[i]))):
                curr_sum += piles[i][j]
                res = max(res, curr_sum + solve(i+1, k-(j+1)))
                
            return res
        
        return solve(0, k)
                