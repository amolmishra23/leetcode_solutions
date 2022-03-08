class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left_end, right_start = None, None
        if n<=1: return 0
        
        for i in range(1, n):
            if arr[i]>=arr[i-1]: continue
            left_end = i-1
            break
        
        if left_end is None: return 0
        
        for i in range(n-2, -1, -1):
            if arr[i]<=arr[i+1]: continue
            right_start = i+1
            break
            
        res = min(
            n-1-left_end, # remove all the elements after left_end
            right_start # remove all the elements before the right_start
        )
        
        l, r = 0, right_start
        
        # now try extending the 2 pointers from our end
        # and verify its viability
        # the logic to move the pointers is similar to binary search one
        while (l<=left_end and r<=n-1):
            if arr[l]<=arr[r]:
                res = min(res, r-l-1)
                l+=1
            else:
                r+=1
        
        return res