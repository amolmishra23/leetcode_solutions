class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def normalize(s):
            seen = dict()
            ans = ""
            nextChr = 'a'
            for c in s:
                if c not in seen:
                    seen[c] = nextChr
                    nextChr = chr(ord(nextChr) + 1)
                ans += seen[c]
            return ans

        return normalize(s) == normalize(t)