class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        We memoize with an array of dicts, dp, such that dp[i][j] stores the number of arithmetic slices (including those with only length 2) whose constant difference is j ending at i. The key is basically to store all 2+-length arithmetic slices (which is helps to build up the solution from its sub-problems) while only adding valid 3+-length slices to the total.

The we iterate over all pairs in the array. Each (A[j], A[i]) is a 2-length slice with constant difference A[i] - A[j] that we've never encountered before, so increment dp[i][A[i] - A[j]] by 1 (but leave the total as is, because its not length 3 or more).

If there are any slices with A[i] - A[j] length that finish at index j (if A[i]-A[j] in dp[j]:), we 'extend' them to index i and add to the total, since any slice that terminated at index j would now have at least length 3 terminating at i.
        """
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                # if at all it occured till j, means i can be combined with all those sequences.
                # in addition can form a new sequence with j. basically (j,i)
                # hence number of AP's ending at i. is dp[j]+1
                dp[i][diff] += dp[j][diff] + 1
                # because now j is surely worth 3 elements. can contribute to our result. 
                res += dp[j][diff]
        
        return res
                
                