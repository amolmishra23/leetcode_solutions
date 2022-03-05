class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(left, right):
            if left > right: return (0, 0)
            
            pickLeft = dp(left+1, right)
            pickRight = dp(left, right - 1)
            
            if piles[left] + pickLeft[1] > piles[right] + pickRight[1]:  # If the left choice has higher score than the right choice
                return piles[left] + pickLeft[1], pickLeft[0]  # then pick left
            
            return piles[right] + pickRight[1], pickRight[0]  # else pick right
        
        alexScore, leeScore = dp(0, len(piles) - 1)
        return alexScore > leeScore