class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp, MOD = {}, (10**9)+7
        for a in sorted(arr):
            # single element tree all can make
            temp = 1
            for b in dp:
                if a%b==0: temp = (temp + dp[b]*dp.get(a//b, 0)) % MOD
            dp[a] = temp
            
        return sum(dp.values())%MOD