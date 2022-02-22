class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def solve(idx, curr, target):
            if target==0:
                self.res.append(list(curr))
                return
            
            if target<0 or idx>=len(arr): return 
            
            solve(idx+1, curr, target)
            curr.append(arr[idx])
            solve(idx, curr, target-arr[idx])
            curr.pop()
        
        self.res = []
        solve(0, [], target)
        return self.res