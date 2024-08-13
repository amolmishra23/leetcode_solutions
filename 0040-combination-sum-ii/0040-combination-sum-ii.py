class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        res = []
        arr.sort()
        
        def dfs(i, curr, total):
            nonlocal res
            if total == target: 
                res.append(list(curr))
                return
            
            if total > target or i == len(arr):
                return
            
            curr.append(arr[i])
            dfs(i+1, curr, total + arr[i])
            curr.pop()
            
            # Skipping candidates[i]
            # In case we have an input like [1,1,1,1,7]. 
            # only valid combination is [1,7]
            while i+1<len(arr) and arr[i]==arr[i+1]: i+=1
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return res