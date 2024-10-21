class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def solve(i, seen):
            if i==len(s):
                return len(seen)
            
            res = 0
            
            for j in range(i, len(s)):
                if s[i:j+1] not in seen:
                    seen.add(s[i:j+1])
                    res = max(res, solve(j+1, seen))
                    seen.remove(s[i:j+1])
                    
            return res
        
        return solve(0, set())