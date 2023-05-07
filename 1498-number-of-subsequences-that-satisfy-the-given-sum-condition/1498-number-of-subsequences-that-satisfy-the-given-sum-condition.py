class Solution:
    def numSubseq(self, A, target):
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        
        while l <= r:
            if A[l] + A[r] > target:
                # everytime we arent less than target, we reduce right pointer
                r -= 1
            else:
                # time to record an answer. Because keeping index l constant, 
                # in the numbers from (r-l), we can have 2**(r-l) subsequences. 
                # meanwhile also keep modding the answer
                res += pow(2, r - l, mod)
                l += 1
        
        return res % mod
    