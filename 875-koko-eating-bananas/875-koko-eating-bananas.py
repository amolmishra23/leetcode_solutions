class Solution:
    def solve(self, k, piles, h):
        total = 0
        
        for i in range(len(piles)):
            q,r = divmod(piles[i], k)
            total += q
            total += 1 if r>0 else 0
        
        return total <= h
        
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l<r:
            mid = l+(r-l)//2
            if self.solve(mid, piles, h):
                r = mid
            else:
                l = mid+1
        
        return l