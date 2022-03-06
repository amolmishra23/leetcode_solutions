class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = [False]*n
        max_ = max(candies)
        
        for i, c in enumerate(candies):
            res[i] = (c+extraCandies>=max_)
            
        return res
            
        