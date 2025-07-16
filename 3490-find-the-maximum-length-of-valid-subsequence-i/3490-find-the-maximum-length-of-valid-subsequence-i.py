class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even, odd = 0, 0
        for num in nums:
            if num%2==0: even+=1
            else: odd+=1

        evenDP, oddDP= 0, 0
        for num in nums:
            if num%2==0:
                evenDP = max(evenDP, oddDP+1)
            else:
                oddDP = max(oddDP, evenDP+1)

        return max(even, odd, evenDP, oddDP)

    def maximumLength1(self, nums: List[int]) -> int:
        n = len(nums)
        dp, res = [[1 for _ in range(2)] for _ in range(n)], 1
        
        for i in range(n):
            for j in range(i):
                key = (nums[i]+nums[j])%2
                dp[i][key] = max(dp[i][key], dp[j][key]+1)
                res = max(res, dp[i][key])

        return res
        
