class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        cnt = 0
        lastNum = 0  # Since nums[i] >= 1, lastNum = 0 is a valid choice to out of range value of nums

        count = Counter(nums)
        for x,y in sorted(count.items()):
            arr.append([x, y])
            
        print(arr)
        
        @lru_cache(None)
        def dp(i, lastPicked):
            if i == len(arr): return 0
            # Dont pick i
            ans = dp(i+1, False)
            
            # Pick i
            """
            Only conditions to be selected. 
            1. if we are at start index.
            2. if last picked and last element was arr[i]-1. Then we dont pick.
            
            Else we try to pick, and to result we try adding arr[i][0]*arr[i][1]
            """
            if i == 0 or not (lastPicked and arr[i-1][0] == arr[i][0]-1):
                ans = max(ans, dp(i+1, True) + arr[i][0] * arr[i][1])
            
            return ans
        
        return dp(0, False)