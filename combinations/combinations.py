class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(arr, low, high, curr, res):
            if len(curr)==k:
                res.append(list(curr))
                return
            
            if low>high:
                return
            
            curr.append(arr[low])
            solve(arr, low+1, high, curr, res)
            curr.pop()
            
            solve(arr, low+1, high, curr, res)
            
        res = []
        solve(list(range(1, n+1)), 0, n-1, [], res)
        return res