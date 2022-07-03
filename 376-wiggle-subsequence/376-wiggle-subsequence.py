class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp_low, dp_high = [1]*n, [1]*n
        
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                # hence we considering high case
                # high subsequence we need longest low subsequence until then
                dp_high[i] = dp_low[i-1]+1
                dp_low[i] = dp_low[i-1]
            elif nums[i]<nums[i-1]:
                # hence we considering low case
                # high subsequence we need longest high subsequence until then
                dp_high[i] = dp_high[i-1]
                dp_low[i] = dp_high[i-1]+1
            else:
                # no increment in this case
                dp_low[i], dp_high[i] = dp_low[i-1], dp_high[i-1]
                
        return max(dp_low[-1], dp_high[-1])