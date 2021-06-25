class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        def solve(arr, idx, curr_path, res, target):
            if len(curr_path)==k and target==0:
                res.add(tuple(curr_path))
                return
            
            if target<0: return 
            
            if idx>=len(arr): return
            
            for i in range(idx, len(arr)):
                # because array is sorted, and we stumble upon a bigger number, we break
                if arr[i]>target: break
                # we cannot use same number twice, hence incrementing index.
                curr_path.append(arr[i])
                solve(arr, i+1, curr_path, res, target-arr[i])
                curr_path.pop()
                
        res = set()
        solve(list(range(1,10)), 0, [], res, target)
        return res