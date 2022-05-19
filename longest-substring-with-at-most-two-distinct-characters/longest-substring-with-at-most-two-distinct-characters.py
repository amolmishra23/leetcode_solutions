class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        start, res = 0, 0
        counts = defaultdict(int)
        max_distinct = 2
        
        for end in range(n):
            counts[s[end]] += 1
            
            if len(counts) > 2:
                counts[s[start]] -= 1
                
                if counts[s[start]] == 0:
                    del counts[s[start]]
                
                start += 1
                
            res = max(res, end - start + 1)
            
        return res