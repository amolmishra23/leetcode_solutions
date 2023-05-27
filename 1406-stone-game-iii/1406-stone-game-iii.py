class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def dp(curr_idx, curr_player):
            if curr_idx >= len(stoneValue): return 0
            res = float("-inf") if curr_player else float("inf")
            curr_sum = 0
            
            for i in range(curr_idx, min(curr_idx+3, len(stoneValue))):
                if curr_player==1:
                    curr_sum += stoneValue[i]
                    res = max(res, curr_sum + dp(i+1, curr_player^1))
                else:
                    curr_sum -= stoneValue[i]
                    res = min(res, curr_sum + dp(i+1, curr_player^1))
                    
            return res
        
        res = dp(0, 1)
        return "Alice" if res>0 else ("Bob" if res<0 else "Tie")
