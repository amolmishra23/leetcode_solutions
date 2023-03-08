class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_required(k):
            res = 0
            
            for pile in piles:
                q,r = divmod(pile,k)
                res+=q
                res+=1 if r else 0
                
            return res
        
        low, high = 1, max(piles)
        
        while low<high:
            mid = low+(high-low)//2
            if hours_required(mid)<=h:
                high=mid
            else:
                low=mid+1
                
        return low