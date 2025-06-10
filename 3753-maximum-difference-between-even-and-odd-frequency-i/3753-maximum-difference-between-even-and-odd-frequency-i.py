class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = max([v for k,v in Counter(s).items() if (v%2)!=0])
        min_even = min([v for k,v in Counter(s).items() if (v%2)==0])
        return max_odd-min_even