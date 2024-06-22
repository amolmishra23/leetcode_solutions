class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = res = 0
        count, n = Counter([0]), len(nums)
        
        for i in range(n):
            prefixsum += nums[i]
            res += count[prefixsum-k]
            count[prefixsum]+=1
            
        return res