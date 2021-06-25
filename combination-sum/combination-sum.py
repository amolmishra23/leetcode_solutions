class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def solve(arr, idx, curr_path, res, target):
            if target==0:
                res.add(tuple(curr_path))
                return
            
            for i in range(idx, len(arr)):
                # because array is sorted, and we stumble upon a bigger number, we break
                if arr[i]>target: break
                # we can use same number twice, hence not incrementing index.
                # only need to operate upon the target
                curr_path.append(arr[i])
                solve(arr, i, curr_path, res, target-arr[i])
                curr_path.pop()
                
        res = set()
        solve(sorted(arr), 0, [], res, target)
        return res