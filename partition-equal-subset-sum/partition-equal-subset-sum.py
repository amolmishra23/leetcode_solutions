class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Basic idea being if we have set 1,2,3,5. Sum being 10. If we can find
        # a subset which sums to 10/2(5), we can partition them equally. 
        n, sum_ = len(nums), sum(nums)
        if sum_%2!=0: return False
        target = sum_//2
        
        # Imagine the dp table like rows accomodating all possible inputs. 
        # Cols accomodating possible sums from 1 to target sum. 
        # dp[i][j] will contain, using numbers till ith index, 
        # is it possible to make the subset sum j
        dp = [[None]*(target+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(target+1):
                # in case i is 0 means making sum from 1 to n, with 0 numbers.
                # Not possible. False in case j is 0 means making sum 0, with
                # all possible index numbers. Possible if we dont choose
                # anything. 
                if i==0 and j==0: dp[i][j] = True
                elif i==0: dp[i][j] = False
                elif j==0: dp[i][j] = True
                # if the number is less than target sum. And we plan on using
                # it. Lets say target is 5, and we used 3. We need to verify
                # for existance of 2 in array. Hence check if j-nums[i-1] is
                # True. In case of ith index, we always use i-1 only because it
                # is a bonded knapsack. Cant resue the ith row ka element.
                # Hence use i-1. 
                elif nums[i-1]<=j: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else: dp[i][j] = dp[i-1][j]
                    
        return dp[n][target]