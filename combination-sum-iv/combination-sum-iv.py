class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Aim of the problem is to calculate how many possible permutations can generate a target sum?
        We go in a deep recursion tree, to see all permutations which can bring us the target sum
        Basically if we have num 3, and target 5. Total permutations is, 3+num of ways to get target(2)
        Hence we solve that over all the numbers and return the result. 
        """
        def solve(nums, target):
            if dp[target] is not None: return dp[target]
            
            res=0
            for num in nums:
                if num<=target: res+=solve(nums, target-num)
                
            dp[target]=res
            return res
        
        dp = [None]*(target+1)
        dp[0]=1
        solve(nums, target)
        return dp[target]