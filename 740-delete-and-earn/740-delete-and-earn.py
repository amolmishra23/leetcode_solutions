class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        
        arr = [(num, count) for num, count in sorted(Counter(nums).items())]
        
        @lru_cache(None)
        def dp(i, lastPicked):
            if i>=len(arr): return 0
            
            res = dp(i+1, False)
            
            if i==0 or (lastPicked and arr[i-1][0]+1==arr[i][0])==False:
                res = max(res, arr[i][0]*arr[i][1] + dp(i+1, True))
                
            return res
        
        return dp(0, False)