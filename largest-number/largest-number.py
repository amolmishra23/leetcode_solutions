import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        compare = lambda a, b: 1 if a+b>b+a else (-1 if a+b<b+a else 0)
        res = sorted(list(map(str, nums)), key = functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(res)))