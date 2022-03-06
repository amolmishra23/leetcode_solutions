class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0]*n
        res[-1] = arr[-1]
        if n==1: return [-1]
        
        for i in range(n-2, -1, -1):
            res[i] = max(arr[i+1], res[i+1])
        
        res[-1] = -1
        
        return res