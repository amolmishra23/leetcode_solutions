class Solution:
    def countBits(self, num):
        res = 0
        
        while num:
            num &= (num-1)
            res += 1
            
        return res
    
    def canSortArray(self, nums: List[int]) -> bool:        
        groups = [(key, list(group)) for key, group in groupby(nums, key=self.countBits)]
        
        maxSoFar = float("-inf")
        for key, group in groups:
            mn, mx = min(group), max(group)
            if mn<maxSoFar: return False
            maxSoFar = mx
            
        return True