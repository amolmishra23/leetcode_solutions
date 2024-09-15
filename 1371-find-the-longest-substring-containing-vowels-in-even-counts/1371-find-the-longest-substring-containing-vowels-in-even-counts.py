class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        
        res, mask = 0, 0
        maskToIdx = {0:-1}
        
        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord("a"))
            if mask in maskToIdx: 
                length = i - maskToIdx[mask]
                res = max(res, length)
            else:
                maskToIdx[mask] = i
                
        return res