class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        @lru_cache(None)
        def solve(idx):
          if idx==len(s): return True
          
          for i in range(idx+1, len(s)+1):
            temp = s[idx:i]
            if temp in wordDict and solve(i): return True
            
          return False
        
        return solve(0)