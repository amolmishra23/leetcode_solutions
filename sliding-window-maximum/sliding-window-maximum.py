from collections import deque

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        res = []
        i, j = 0, 0
        q = deque()

        while j<len(arr):
            while q and arr[q[-1]]<arr[j]: q.pop()
            q.append(j)

            if j-i+1<k:
                j+=1
            else:
                res.append(arr[q[0]])
                if q and q[0]==i: q.popleft()
                i+=1
                j+=1

        return res