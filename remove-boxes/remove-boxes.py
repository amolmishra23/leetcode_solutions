class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def mcm(dp, boxes, l, r, s):
            if l>r: return 0
            elif l==r: return (s+1)**2
            elif dp[l][r][s] is not None: return dp[l][r][s]
            else:
                max_ = (s+1)**2 + mcm(dp, boxes, l+1, r, 0)

                for m in range(l+1, r+1):
                    if boxes[m]==boxes[l]:
                        max_=max(max_, mcm(dp, boxes, l+1, m-1, 0)+mcm(dp, boxes, m, r, s+1))

                dp[l][r][s] = max_
                return dp[l][r][s]
        
        if not boxes or len(boxes)==0: return 0
        
        n = len(boxes)
        
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return mcm(dp, boxes, 0, n-1, 0)
    
    