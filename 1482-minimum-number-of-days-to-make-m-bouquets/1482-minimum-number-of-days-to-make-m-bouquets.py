class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def solve(mid):
            curr_streak = 0
            bouquets = m
            
            for i in bloomDay:
                if i<=mid:
                    curr_streak+=1
                    if curr_streak==k: 
                        bouquets-=1
                        curr_streak=0
                    if bouquets==0: return True
                else:
                    curr_streak=0
                
            return bouquets==0
    
        if len(bloomDay)<m*k: return -1
        lo, hi = 1, max(bloomDay)

        res = -1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if solve(mid):
                res = mid
                hi = mid-1
            else:
                lo = mid+1
        
        return res