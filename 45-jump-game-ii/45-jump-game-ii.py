class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def solve(idx):
            if idx >= n-1: return 0
            
            res = float('inf')
            for i in range(1, nums[idx]+1):
                res = min(res, 1+solve(idx+i))
                
            return res
        
        return solve(0)