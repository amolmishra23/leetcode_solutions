class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        def dfs(num):
            if num in dp: return dp[num]
            
            # in subproblem no need to break the number
            # in actual problem we definitely need to break, hence this condition
            res=0 if num==n else num
            
            for i in range(1, num):
                val = dfs(i) * dfs(num-i)
                res = max(res, val)
                
            dp[num] = res
            return dp[num]
        
        return dfs(n)