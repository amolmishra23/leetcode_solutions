class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(sx-fx), abs(sy-fy)
        if dx==0 and dy==0 and t==1: return False
        return min(dx,dy)+abs(dx-dy) <= t