class Solution:
    def findMaxForm(self, arr: List[str], m: int, n: int) -> int:
        def solve(arr, m, n, idx, res):
            # top down dp. 
            if (m, n, idx) in res: return res[(m, n, idx)]
            
            # we have reached the end and cant add anymore value.
            if idx>=len(arr) or m+n==0: return 0
            
            # counting the number of occurences of 0 and 1 in the current element
            count = Counter(arr[idx])
            temp = 0
            
            if count["0"]<=m and count["1"]<=n: 
                # including this particular element and counting the rest
                temp=1+solve(arr, m-count["0"], n-count["1"], idx+1, res)
            
            # not including this element
            res[(m,n,idx)] = max(temp, solve(arr, m, n, idx+1, res))
            
            return res[(m,n,idx)]
        
        res = {}
        return solve(arr, m, n, 0, res)