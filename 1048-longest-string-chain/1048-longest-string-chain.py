class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words=set(words)
        
        @lru_cache(None)
        def dp(word):
            res = 1
            for i in range(len(word)):
                temp = word[:i] + word[i+1:]
                if temp in words:
                    res = max(res, dp(temp)+1)
            return res
        
        return max(dp(word) for word in words)