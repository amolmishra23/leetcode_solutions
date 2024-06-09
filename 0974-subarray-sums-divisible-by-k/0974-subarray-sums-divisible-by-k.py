class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = Counter([0])
        curr_sum, res = 0, 0
        
        for x in nums:
            curr_sum = (curr_sum + x)%k
            res += prefix_sums[curr_sum]
            prefix_sums[curr_sum] += 1
            
        return res