class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @lru_cache(None)
        def dfs(l, r):
            """
            Whole idea is that, we assume we are bursting the ith ball in end. 
            hence bursting ith baloon, we get nums[i]*nums[l-1]*nums[r+1]
            other baloons bursted meanwhile, can be found by dfs(l, i-1) and dfs(i+1, r)
            and keep updating max score in res variablle to be returned
            """
            if l>r: return 0
            
            res = float("-inf")
            
            for i in range(l, r+1):
                coins = nums[i]*nums[l-1]*nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                res = max(res, coins)
                
            return res

        return dfs(1, len(nums)-2)