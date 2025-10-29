class Solution(object):
    def smallestNumber(self, n):
        res = 1
        while res<n: res = (res<<1) | 1
        return res