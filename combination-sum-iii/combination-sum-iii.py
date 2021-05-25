class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def solve(x, stack, target):
            if len(stack)==k:
                if target==0: res.append(list(stack))
                return
            
            for i in range(x+1, 10):
                if i<=target:
                    solve(i, stack+[i], target-i)
                else:
                    return
                    
        solve(0, [], n)
        return res