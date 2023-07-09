class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # to split in k bags, do k-1 cuts. 
        # such cuts which lead to minimum and maximum values. 
        # their difference is our solution
        distribution = [x+y for x, y in zip(weights[:-1], weights[1:])]
        return sum(nlargest(k-1, distribution)) - sum(nsmallest(k-1, distribution))