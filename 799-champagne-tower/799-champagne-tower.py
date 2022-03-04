class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        At (2,2), it will fall from (1,1)
        At (2,1), it will fall from (1,0) and (1,1)
        Same logic, a glass will contain dp(r-1,c-1) and dp(r-1,c)
        
        We additionally subtract 1 because only from the excess a glass has, we will be getting the drink. 
        
        Now, because the drink falls on 2 glasses, we get half the drink. Hence subtract it by half. 
        """
        @lru_cache(None)
        def dp(r, c):
            if c<0 or c>r: return 0
            if r==0 and c==0: return poured
            return max(dp(r-1, c-1)-1, 0)/2 + max(dp(r-1,c)-1, 0)/2
        
        # wrapping it by min 1, because excess is anyways overflown down. 
        return min(dp(query_row, query_glass), 1)