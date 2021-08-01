class Solution:
    def trap(self, arr: List[int]) -> int:
        def greatest_right(arr):
            res = [None]*len(arr)
            max_=0
            
            for i in range(len(arr)-1, -1, -1):
                res[i] = max_
                max_ = max(max_, arr[i])
                
            return res
        
        def greatest_left(arr):
            res = [None]*len(arr)
            max_=0
            
            for i in range(len(arr)):
                res[i] = max_
                max_ = max(max_, arr[i])
                
            return res
        
        gr = greatest_right(arr)
        gl = greatest_left(arr)
        
        res = 0
        for i in range(len(arr)):
            # it comes down to whichever is highest on left/right subtract with arr[i]
            # we cannot have negative water, hence max it with 0
            # total of all this, is the total rain water that can be trapped. 
            val = max(min(gr[i], gl[i])-arr[i], 0)
            res += val
            
        return res
            