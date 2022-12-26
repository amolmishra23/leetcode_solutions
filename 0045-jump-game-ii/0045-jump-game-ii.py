class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def can_reach(idx):
            if idx>=len(nums)-1: return 0
            
            cost = float('inf')
            
            for i in range(1, nums[idx]+1):
                cost = min(cost, 1 + can_reach(idx+i))
                
            return cost
        
        return can_reach(0)