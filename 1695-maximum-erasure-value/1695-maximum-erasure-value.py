class Solution:
    def construct_prefix_sum(self, nums):
        self.prefix_sum = [0]*(len(nums)+2)
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i]+nums[i]
            
    def prefix_sum_cal(self, start, end):
        return self.prefix_sum[end]-self.prefix_sum[start-1]
    
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        curr_sum, max_sum, prev_idx = 0, 0, {}
        
        for end in range(len(nums)):
            if nums[end] in prev_idx:
                idx = prev_idx[nums[end]]
                while start<=idx:
                    curr_sum -= nums[start]
                    del prev_idx[nums[start]]
                    start+=1
            prev_idx[nums[end]] = end
            curr_sum += nums[end]
            max_sum = max(max_sum, curr_sum)
            
        return max_sum