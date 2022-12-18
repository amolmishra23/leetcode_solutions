class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        def ngr(arr):
            n, res, stk = len(arr), [None]*len(arr), []
            
            for i in range(n-1, -1, -1):
                while stk and arr[stk[-1]]<=arr[i]: stk.pop()
                res[i] = stk[-1] if stk else -1
                stk.append(i)
                
            return res
        
        def dngr(arr):
            n_g_r = ngr(arr)
            res = [None]*len(arr)
            
            for i in range(len(arr)):
                res[i] = max(n_g_r[i]-i, 0)
                
            return res
        
        return dngr(arr)