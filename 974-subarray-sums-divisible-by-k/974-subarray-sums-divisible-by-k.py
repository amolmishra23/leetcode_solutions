class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        Very easy question
        https://www.youtube.com/watch?v=kiHpKTfovRY
        To check divisibility all we bother is, mod with k, should be 0
        Or if we got mod as 2, after sometime if we again 2 means. Elements in between%k=0. 
        So this subarray is divisible by k
        
        If we get mod as 2 multiple times, to find number of subarrays. An easy trick is, keep adding whatever subarray count is currently.
        Hence we first add to res, using preSums.get(s, 0)
        Finally we cache the count of s encountered. 
        """
        preSums = {0: 1}
        s = 0
        res = 0
        for x in A:
            s = (s + x) % K
            res += preSums.get(s, 0)
            preSums[s] = preSums.get(s, 0) + 1
        return res