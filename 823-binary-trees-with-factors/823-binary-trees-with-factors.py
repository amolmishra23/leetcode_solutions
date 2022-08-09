class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Logic from https://www.youtube.com/watch?v=BRGz8ArRiPA
        Solve it using dp.
        Every num in arr, we need to compare it against all others in array. 
        To check if num%other_num==0 and num//other_num is in array. So we have got 2 kids for the num.
        Now number of ways to create num, is equal to product of number of ways we can create its kids. 
        
        Answer could be large, hence we keep modding it. 
        """
        arr, MOD = set(arr), 10**9+7
        
        @lru_cache(None)
        def solve(num):
            ans = 1
            for n in arr:
                if num%n==0 and num//n in arr:
                    ans = (ans + solve(n)*solve(num//n))%MOD
            return ans
        
        return sum([solve(n) for n in arr])%MOD