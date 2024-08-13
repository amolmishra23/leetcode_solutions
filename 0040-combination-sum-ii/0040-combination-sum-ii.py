class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        res = set()
        def solve(idx, curr_path, target):
            nonlocal res
            if target==0:
                res.add(tuple(curr_path))
                return
            
            if idx>=len(arr) or target<0: return 
            
            for i in range(idx, len(arr)):
                if i>idx and arr[i]==arr[i-1]: continue
                if arr[i]>target: return
                curr_path.append(arr[i])
                solve(i+1, curr_path, target-arr[i])
                curr_path.pop()
        
        arr.sort()
        solve(0, [], target)
        return res