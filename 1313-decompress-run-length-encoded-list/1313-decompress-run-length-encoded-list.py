class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(0, n, 2):
            freq, num = nums[i], nums[i+1]
            res.extend([num]*freq)
            
        return res