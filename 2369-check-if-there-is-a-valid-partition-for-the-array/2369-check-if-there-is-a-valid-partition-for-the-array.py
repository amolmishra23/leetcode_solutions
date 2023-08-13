class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def isValidPartition(idx):
            if idx>=len(nums): return True
            
            res = []
            if idx+1<len(nums) and nums[idx]==nums[idx+1] and isValidPartition(idx+2):
                return True
            
            if idx+2<len(nums) and nums[idx]==nums[idx+1]==nums[idx+2] and isValidPartition(idx+3):
                return True
            
            if idx+2<len(nums) and nums[idx]+2==nums[idx+1]+1==nums[idx+2] and isValidPartition(idx+3):
                return True
            
            return False
        
        return isValidPartition(0)