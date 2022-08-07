class Solution:
    def countVowelPermutation(self, n: int) -> int:
        map_ = {
            ".": ["a", "e", "i", "o", "u"],
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["u", "i"],
            "u": ["a"]
        }
        
        @lru_cache(None)
        def dp(i, last):
            if i==n: return 1
            res = 0
            for nxt in map_[last]:
                res = (res + dp(i+1, nxt))%1_000_000_007
            return res
        
        return dp(0, ".")