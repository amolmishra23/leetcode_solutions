class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows<=1: return s
        res = [
            [] for _ in range(num_rows)
        ]
        
        dir = 1
        i = 0
        for chr in s:
            res[i].append(chr)
            i+=dir
            if i==0 or i==num_rows-1:
                dir = -dir
            
        
        return ''.join(sum(res, []))
            