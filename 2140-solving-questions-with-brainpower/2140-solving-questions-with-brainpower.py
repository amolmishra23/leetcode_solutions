class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(idx):
            if idx>=len(questions): return 0
            return max(dp(idx+1), questions[idx][0]+dp(idx+questions[idx][1]+1))
                       
        return dp(0)