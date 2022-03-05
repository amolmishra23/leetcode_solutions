class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        ones_count = 0
        window_start = 0
        res = 0
        
        for window_end in range(len(A)):
            curr = A[window_end]
            if curr: ones_count += 1
                
            while ((window_end-window_start+1)-ones_count)>k:
                if A[window_start]==1: ones_count-=1
                window_start += 1
            
            res = max(res, window_end-window_start+1)
            
        return res