class Solution:
    def nsr(self, arr):
        n, res = len(arr), [None]*len(arr)
        stk = []

        for i in range(n-1, -1, -1):
            while stk and arr[stk[-1]]>=arr[i]: stk.pop()
            res[i] = stk[-1] if stk else n
            stk.append(i)

        return res

    def nsl(self, arr):
        n, res = len(arr), [None]*len(arr)
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]]>=arr[i]: stk.pop()
            res[i] = stk[-1] if stk else -1
            stk.append(i)

        return res

    def largestRectangleArea(self, arr):
        if not arr: return 0
        if len(arr)==1: return arr[0]

        nsr, nsl = self.nsr(arr), self.nsl(arr)

        width = []

        for l,r in zip(nsl, nsr):
            width.append(max(r-l-1, 0))

        res = 0
        for h, w in zip(arr, width):
            res=max(res, h*w)

        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]): return 0
        res = 0

        m, n = len(matrix), len(matrix[0])
        prev = [0]*n

        for i in range(m):
            for j in range(n):
                prev[j] = prev[j]+1 if matrix[i][j]=="1" else 0
            res = max(res, self.largestRectangleArea(prev))

        return res
