class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        lo, hi = 0,0
        curr = 0

        for d in differences:
            curr += d
            lo = min(lo, curr)
            hi = max(hi, curr)

        return max(0, (upper-lower)-(hi-lo)+1)