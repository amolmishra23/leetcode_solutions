class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0: return -1

        rem = 0

        for l in range(1, k+1):
            rem = (rem*10 + 1)%k
            if rem==0: return l

        return -1