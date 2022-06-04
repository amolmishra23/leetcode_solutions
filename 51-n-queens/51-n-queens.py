class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:      
        def solve(arr, idx, curr, res):
            n = len(arr)
            if idx==n:
                res.append(list(curr))
                return 
            
            for i in range(n):
                arr[idx] = i
                if is_valid(arr, idx):
                    tmp = ["."]*n
                    tmp[i] = "Q"
                    solve(arr, idx+1, curr+["".join(tmp)], res)
        
        def is_valid(arr, idx):
            # diagonal can be verified using if x coordinates abs diff equals y coordinates abs diff
            # col clashing can be verified using comparing val of arr, at all 'i' against 'idx'
            for i in range(idx):
                if abs(arr[idx]-arr[i]) == (idx-i) or arr[i]==arr[idx]: return False
            return True
        
        res = []
        solve([-1]*n, 0, [], res)
        return res
        