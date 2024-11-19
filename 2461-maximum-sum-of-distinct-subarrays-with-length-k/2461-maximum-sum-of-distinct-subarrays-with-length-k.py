class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, prev_idx = 0, {}
        curr_sum = 0
        
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            i = prev_idx.get(nums[r], -1)
            
            while l<=i or r-l+1>k:
                curr_sum -= nums[l]
                l+=1
            
            if r-l+1 == k:
                res = max(res, curr_sum)
                
            prev_idx[nums[r]] = r
            
        return res
        
    def maximumSubarraySum1(self, nums: List[int], k: int) -> int:
        res, count = 0, Counter()
        curr_sum, l = 0, 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            count[nums[r]]+=1
            
            if r-l+1 > k:
                count[nums[l]]-=1
                curr_sum -= nums[l]
                if count[nums[l]]==0: del count[nums[l]]
                l += 1
            
            if r-l+1 == len(count) == k:
                res = max(res, curr_sum)
                
        return res