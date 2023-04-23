class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         MOD = (10**9)+7
        
#         @lru_cache(None)
#         def dp(curr_idx):
#             if curr_idx >= len(s): return 1
#             if s[curr_idx]=="0": return 0
#             res, curr_val = 0, 0
            
#             for i in range(curr_idx, len(s)):
#                 curr_val = 10 * curr_val + (ord(s[i]) - ord('0'))
#                 if curr_val <= k:
#                     res = (res+dp(i+1))%(MOD)
            
#             return res % MOD
        
#         return dp(0)

        def numberOfArrays(self, s: str, k: int) -> int:
            m, n = len(str(k)), len(s)
            dp = [1] * (n + 1)
            #find out number of ways for each ending.
            for i in range(n):
                res, cur = 0, ""
                #For each ending digit i, we traves back, to find all the valid numbers which is no larger than k, and ending with this digit i.
                for idx in range(i, max(-1, i - m), -1):  # In case we transpass the first digit.
                    cur = s[idx] + cur
                    if cur[0] != "0" and int(cur) <= k: # A number is valid if it has no leading zero and no larger than k.
                        res += dp[idx]                          # Whenever we have a valid ending number, we add the dp[idx] to dp[i].
                if res == 0:
                    return 0
                else:
                    dp[i + 1] = res % (10 ** 9 + 7)
            return dp[-1]

