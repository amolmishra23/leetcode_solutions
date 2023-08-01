class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, comb):
            if len(comb)==k:
                res.append(list(comb))
                return
            
            if start>n: return 
            
            # not using the current number
            backtrack(start+1, comb)
            
            # using the current number
            comb.append(start)
            backtrack(start+1, comb)
            comb.pop()
            
        backtrack(1, [])
        return res
            