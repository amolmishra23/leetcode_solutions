class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count, res = 0, 0
        for c in allowed: count |= (1<<(ord(c) - ord("a")))    
            
        for word in words:
            valid = 1
            for c in word:
                if (count & (1 << (ord(c) - ord("a")))) == 0: 
                    valid = 0; break
            res += valid
            
        return res
                