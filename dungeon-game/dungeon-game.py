class Solution:
    def calculateMinimumHP(self, arr: List[List[int]]) -> int:
        def solve(arr, i, j, dp):
            # this is the overflow base condition
            if i>=m or j>=n: return float('inf')
            
            if (i, j) in dp: return dp[(i, j)]
            
            # which is the next cheapest path to traverse. 
            next_ = min(solve(arr, i+1, j, dp), solve(arr, i, j+1, dp))
            
            # we should have atleast 1 health extra when we reach destination
            if next_ == float('inf'): next_=1
            
            # example when we reach (2,2) we atleast need 6 health.
            # 1-(-5) = 1+5 = 6
            dp[(i, j)] = max(next_-arr[i][j],1)
            return dp[(i,j)]
                
        
        if not arr or len(arr)==0 or len(arr[0])==0: return 0
        m, n = len(arr), len(arr[0])
        dp = {}
        return solve(arr, 0, 0, dp)