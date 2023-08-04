class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        
        @lru_cache(None)
        def solve(idx):
            if idx==n: return True
            
            for i in range(idx+1, n+1):
                curr_word = s[idx: i]
                if curr_word in wordDict:
                    if solve(i): return True
                    
            return False
        
        return solve(0)