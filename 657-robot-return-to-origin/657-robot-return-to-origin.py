from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves); return count["U"]==count["D"] and count["L"]==count["R"]
        