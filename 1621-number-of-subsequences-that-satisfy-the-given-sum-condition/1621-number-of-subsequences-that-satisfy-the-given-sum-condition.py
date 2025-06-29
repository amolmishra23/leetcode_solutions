class Solution:
    def numSubseq(self, A: List[int], target: int) -> int:
        A.sort()
        n = len(A)
        l, r = 0, n-1
        res, MOD = 0, 10**9+7

        while l<=r:
            if A[l]+A[r]>target:
                r-=1
            else:
                subsequence_count = (pow(2, r-l))%MOD
                res = (res + subsequence_count)%MOD
                l+=1

        return res
