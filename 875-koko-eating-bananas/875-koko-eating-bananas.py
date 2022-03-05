class Solution:
    """
    https://www.youtube.com/watch?v=UmuW0C4eFYg
    """
    def solve(self, k, piles, h):
        # finding total number of hours it takes
        # if we restrict to eating k banana maximum per hour
        # lets say we have 7 banana. At speed of 3. We will take 3 hrs. 
        total = 0
        
        for i in range(len(piles)):
            q,r = divmod(piles[i], k)
            total += q
            total += 1 if r>0 else 0
        
        return total <= h
        
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # our aim is to eat banana's nearest to guard return time. 8 hours. 
        # We can eat anywhere between 1 and maximum number of banana's
        l, r = 1, max(piles)
        
        while l<r:
            mid = l+(r-l)//2
            if self.solve(mid, piles, h):
                r = mid
            else:
                l = mid+1
        
        return l