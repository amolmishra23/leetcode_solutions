class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = prev = curr = 0
        
        for bit in nums:
            if bit:
                curr += 1
                res = max(res, curr+prev)
            else:
                prev, curr = curr, 0
                
        return res if res!=len(nums) else res-1