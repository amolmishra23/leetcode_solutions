class Solution:
    def ngr(self, arr):
        n, res = len(arr), [None]*len(arr)
        stk = []
        
        for i in range(n-1, -1, -1):
            while stk and arr[stk[-1]]<=arr[i]: stk.pop()
            res[i] = stk[-1] if stk else float('-inf')
            stk.append(i)
            
        return res
    
    def dngr(self, arr):
        ngr = self.ngr(arr)
        res = [None]*len(arr)
        
        for i in range(len(arr)):
            res[i] = max(ngr[i]-i, 0)
            
        return res
        
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        return self.dngr(arr)