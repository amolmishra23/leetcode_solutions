class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def solve(target):
            if target==0: return 1
            
            res = 0
            for n in nums:
                if n<=target: 
                    res += solve(target-n)
                    
            return res
        
        return solve(target)