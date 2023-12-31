class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occ, res = {}, float("-inf")
        
        for i, ch in enumerate(s):
            if ch not in first_occ: first_occ[ch]=i
            else: res = max(res, i-first_occ[ch]-1)
                
        return -1 if res==float("-inf") else res