class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return self.dfs(s, 0, "", 0, k)
    
    @lru_cache(None)
    def dfs(self, s, start, prev_char, prev_count, remains):
        if remains < 0: return float('inf')
        if start == len(s):
            return 0
        if s[start] == prev_char:
            inc = 1 if prev_count in {1, 9, 99} else 0
            return inc + self.dfs(s, start+1, prev_char, prev_count + 1, remains)
        else:
            # keep it (starting a new streak from here)
            ans1 = self.dfs(s, start+1, s[start], 1, remains) + 1
            # remove it (removing the current character. So we have remains-1 attempt left)
            ans2 = self.dfs(s, start+1, prev_char, prev_count, remains-1)
            return min(ans1, ans2)
