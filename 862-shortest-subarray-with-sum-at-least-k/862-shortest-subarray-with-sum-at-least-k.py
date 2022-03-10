class Solution:
    def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            # curr prefix sum
            cur += a
            
            # we have a deque to contain monotonically increasing elements.
            # here we kind sum of curr window is bigger than K. 
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            
            # to maintain monotonic, we have to pop out all the elements smaller than curr element
            # as curr element is must to append.
            while d and cur <= d[-1][1]:
                d.pop()
            
            # appending the current element. 
            d.append([i + 1, cur])
            
        return res if res < float('inf') else -1