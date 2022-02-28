class Solution:
    def findUnsortedSubarray(self, a: List[int]) -> int:
        """
        traverse entire array where elem's not sorted and find minimum most element
        similar way find max element not sorted.
        find the position of 1st element greater than min_most unsorted elem
        find the position of 1st element less than max_most unsorted elem
        return the difference of positions, as thats our unsorted array
        """
        
        n = len(a)
        start, end = float('inf'), float('-inf')
        for i in range(n-1):
            if a[i]>a[i+1]:
                start = min(start, a[i+1])
        
        for i in range(n-1, 0, -1):
            if a[i]<a[i-1]:
                end = max(end, a[i-1])
        
        l, r = 0,0
        for i in range(0, n):
            if a[i]>start:
                l = i;
                break
        
        for i in range(n-1, -1, -1):
            if a[i]<end:
                r = i
                break

        return r-l+1 if r-l>0 else 0