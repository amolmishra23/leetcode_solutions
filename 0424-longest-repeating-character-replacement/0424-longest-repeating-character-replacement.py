from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        count = Counter()
        max_len, res = 0, 0
        
        for window_end in range(len(s)):
            last_char = s[window_end]
            count[last_char] += 1
            max_len = max(max_len, count[last_char])
            
            if ((window_end-window_start+1) - max_len)>k:
                count[s[window_start]]-=1
                window_start += 1
            else:
                res = max(res, (window_end-window_start+1))
        
        return res