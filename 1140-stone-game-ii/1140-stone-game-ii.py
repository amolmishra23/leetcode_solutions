class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def solve(idx, m, player):
            if idx>=len(piles): return 0
            if player:
                return max(
                    [sum(piles[idx:idx+x]) + solve(idx+x, max(m, x), player^1) for x in range(1, 2*m+1)]
                )
            else:
                return min(
                    [solve(idx+x, max(m,x), player^1) for x in range(1, 2*m+1)]
                )
            
        return solve(0, 1, 1)