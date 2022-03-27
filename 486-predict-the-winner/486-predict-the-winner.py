class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def helper(s, e):
            if s==e: return nums[s]
            
            front_picked = nums[s] - helper(s+1, e)
            back_picked = nums[e] - helper(s, e-1)
            
            return max(front_picked, back_picked)
        
        return helper(0, len(nums)-1) >= 0