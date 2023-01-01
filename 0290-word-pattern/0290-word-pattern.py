class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return [pattern.index(p) for p in pattern]==[s.split().index(x) for x in s.split()]