class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map_, prefix_mod = {0:-1}, 0
        
        for i, n in enumerate(nums):
            prefix_mod = (prefix_mod+n)%k
            if prefix_mod not in map_: map_[prefix_mod] = i
            elif i-map_[prefix_mod]>=2: return True
        
        return False