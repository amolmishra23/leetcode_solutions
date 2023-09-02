class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        
        @lru_cache(None)
        def solve(idx):
            if idx>=len(s): return 0
            
            # break at s
            res = 1+solve(idx+1)
            
            # not break at s
            for i in range(idx+1, len(s)+1):
                temp = s[idx: i]
                if temp in dictionary:
                    res = min(res, solve(i))
            
            return res
        
        return solve(0)