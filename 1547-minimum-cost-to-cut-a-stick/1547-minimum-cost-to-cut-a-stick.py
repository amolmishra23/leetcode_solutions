class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Problem intuition is that, everytime we cut stick of length x. "x" is added to score
        To make it work efficiently with our dp function, lets add coordinates 0, n to the cuts. 
        Now everytime we can cut at all locations (k) between (i) and (j)
        We try to find the minimum answer
        """
        @lru_cache(None)
        def dp(i, j):
            return 0 if j-i<=1 else min(cuts[j]-cuts[i] + dp(i, k)+dp(k, j) for k in range(i+1, j))
        cuts.extend([0, n]); cuts.sort()
        return dp(0, len(cuts)-1)