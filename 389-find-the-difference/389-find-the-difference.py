class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0: return t
        return chr(reduce(operator.xor, map(ord, s)) ^ reduce(operator.xor, map(ord, t)))