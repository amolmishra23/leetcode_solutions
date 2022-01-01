class Solution:
    def countPoints(self, rings: str) -> int:
        count = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            count[int(rings[i+1])].add(rings[i])
            
        res = 0
        for val in count:
            res += 1 if len(val)==3 else 0
            
        return res