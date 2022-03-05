class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res, cur = 0, 0
        
        for ch in s:
            val = widths[ord(ch)-ord('a')]
            res += 1 if val+cur>100 else 0
            cur = val if val+cur>100 else val+cur
        
        return (res+1, cur)