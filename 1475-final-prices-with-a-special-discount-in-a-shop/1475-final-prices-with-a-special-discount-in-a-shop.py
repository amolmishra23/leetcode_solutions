class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        for i, p in enumerate(prices):
            while stk and prices[stk[-1]] >= p:
                prices[stk.pop()]-=p
            stk.append(i)
        return prices