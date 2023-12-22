class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros, res = Counter(s)["1"], 0, 0
        
        for ch in s[:-1]:
            zeros, ones = zeros+(ch=="0"), ones-(ch=="1")
            res = max(res, zeros+ones)
            
        return res