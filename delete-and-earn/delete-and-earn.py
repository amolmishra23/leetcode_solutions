class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # using counter here, because every number will give us points, equal to its number of occurence.
        # more like if 4 occured 4 times, we get 16 points. 
        count = Counter(nums)
        
        # because max we can get between 1-10000 numbers. array for easy access. 
        dp = [0]*10005
        
        # if we have just 1 and 2 numbers, its base conditions
        dp[1]=count[1]
        # either we can take 1 or 2, not both
        dp[2]=max(count[1], count[2]*2)
        
        for i in range(3, 10005):
            # logic is very similar to the house robber problem. 
            # if we take current number, it contributes points equal to i*count[i]
            dp[i] = max(count[i]*i+dp[i-2], dp[i-1])
            
        # result is either including or excluding the pre-final number. 
        return max(dp[10003], dp[10004])
        
        