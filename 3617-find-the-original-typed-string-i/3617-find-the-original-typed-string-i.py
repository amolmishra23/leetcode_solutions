class Solution:
    def possibleStringCount(self, word: str) -> int:
        res, prev = 1, None

        for i, ch in enumerate(word):
            if ch==prev: res += 1
            prev=ch

        return res

