class Solution:
    def getOperations(self, n):
        res, ops = 0, 0
        power = 1

        while power<=n:
            # Starting in the range
            l = power
            # Ending in the range before next power of 4
            r = min(n, power*4-1)

            # increment by 1
            ops += 1

            # numbers from l to 4 need ops to come down to 0
            res += (r-l+1) * ops

            # For the next iteration
            power *= 4

        return res

    def minOperations(self, queries: List[List[int]]) -> int:
        # if we have odd elements, we need 1 operation extra
        return sum((self.getOperations(r) - self.getOperations(l-1) + 1)//2 for l,r in queries)