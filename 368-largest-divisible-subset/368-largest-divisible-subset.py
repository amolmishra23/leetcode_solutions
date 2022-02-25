class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Very similar to the Longest increasing subsequence problem
        
        # sorting the numbers brings down the time complexity to O(n**2), in worst case
        # as we need to do just 1 operation i%j==0, not the opposite
        nums.sort()
        n = len(nums)
        
        # dp stores, whats the longest path for this index
        # path stores, from which path are we coming
        dp, path = [1]*n, [-1]*n
        
        # max value encountered so far. Helps in starting the result from that index
        max_ = 0
        
        for i in range(1, n):
            for j in range(i):
                # if condition is fulfilled, like LIS we store the path(from which index are we coming)
                # increase the dp value of the curr index too 
                if nums[i]%nums[j]==0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    path[i] = j
            
            # updating the max_ if any change, based on value in dp array
            if dp[i] > dp[max_]: max_ = i
        
        # finding the result. traversing backwards from the path. 
        res = []
        while max_>=0:
            res.append(nums[max_])
            max_ = path[max_]
            
        return res[::-1]
        
        