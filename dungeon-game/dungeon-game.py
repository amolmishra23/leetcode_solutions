class Solution:
    def calculateMinimumHP(self, arr: List[List[int]]) -> int:
        def solve(i, j, arr, res):
            if i>len(arr)-1 or j>len(arr[0])-1: return float('inf')
            
            if (i,j) in res: return res[(i,j)]
            
            next_ = min(solve(i+1, j, arr, res), solve(i, j+1, arr, res))
            
            if next_==float('inf'): next_=1
            
            temp = max(next_-arr[i][j], 1)
            res[(i, j)] = temp
            return temp
        
        if not arr or len(arr)==0 or len(arr[0])==0: return 0
        res = {}
        return solve(0, 0, arr, res)