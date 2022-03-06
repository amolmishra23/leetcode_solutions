import collections

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        res = -1
        for elem, count in counter.items():
            if elem==count: res=max(res, elem)
        return res