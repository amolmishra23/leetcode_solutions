class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l, r = 0, n-1
        
        # Number of elements missing before an index
        missing_count = lambda arr, idx: arr[idx]-(idx+1)
        
        # Keep moving based on to find the closest index to missing k elements
        # formula to find number of missing elements before an idx in missing_count
        while l<=r:
            m = l+(r-l)//2
            count = missing_count(arr, m)
            
            # If we have more than k elements, we move search on left side
            if count >= k:
                r = m-1
            # else move on the right side
            else:
                l = m+1
        
        # Tackling edge case when element is missing from beginning of arr
        if r==-1: return k
        
        # To find missing number, add the lower bound to 
        # diff with number of elements already missing. 
        return arr[r] + k-missing_count(arr, r)