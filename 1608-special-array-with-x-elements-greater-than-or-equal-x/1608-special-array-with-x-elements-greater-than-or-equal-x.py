class Solution:
    def specialArray(self, arr: List[int]) -> int:
        arr.sort()
        def count(arr, val):
            idx = bisect.bisect_left(arr, val)
            return len(arr)-idx
        
        lo, hi = 0, len(arr)
        while lo<=hi:
            mi = lo + (hi-lo)//2
            g_count = count(arr, mi)
            if g_count == mi: return mi
            elif g_count > mi: lo = mi+1
            else: hi = mi - 1
                
        return -1 
    
    def specialArray1(self, nums: List[int]) -> int:
        count = [0]*(len(nums)+1)
        
        for n in nums:
            idx = min(len(nums), n)
            count[idx] += 1
            
        right_count = 0
        for i in range(len(nums), -1, -1):
            right_count += count[i]
            if i == right_count: return right_count
            
        return -1