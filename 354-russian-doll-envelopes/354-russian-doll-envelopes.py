class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Learn the concept from: 
        https://leetcode.com/problems/longest-increasing-subsequence/discuss/1636162/java-binary-search-stepwise-explanation
        (using binary search to find LIS faster than DP)
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        def lis(arr):
            res = [1]*len(arr)
            for i in range(1, len(arr)):
                for j in range(i):
                    if arr[j][0]<arr[i][0] and arr[j][1]<arr[i][1]:
                        res[i] = max(res[i], res[j]+1)
            return max(res)
        
        def lis2(arr):
            seq, res = [float('inf')]*(len(arr)+1), 0
            seq[0] = -float('inf')
            for _, h in arr:
                pos = bisect.bisect_left(seq, h)
                res = max(res, pos)
                if seq[pos] > h:
                    seq[pos] = h
            return res
        
        return lis2(envelopes)