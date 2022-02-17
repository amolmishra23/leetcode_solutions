class Solution:
    # this problem is to be solved using unbounded knapsack
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        def solve(i, target, currpath):
            if target==0:
                self.res.add(tuple(currpath))
                return 
            
            for i in range(i, len(can)):
                if can[i]>target: break
                currpath.append(can[i])
                solve(i, target-can[i], currpath)
                currpath.pop()
                
        self.res = set()
        can.sort()
        solve(0, target, [])
        return self.res