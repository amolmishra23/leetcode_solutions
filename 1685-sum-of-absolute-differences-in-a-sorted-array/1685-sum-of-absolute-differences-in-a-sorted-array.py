class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, prefix_sum, res = len(nums), [0], []
        
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
            
        for i, num in enumerate(nums):
            res.append((i*num - prefix_sum[i]) +(prefix_sum[-1]-prefix_sum[i] - (n-i)*num))
            
        return res