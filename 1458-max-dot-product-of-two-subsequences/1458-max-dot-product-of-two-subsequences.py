class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i==len(nums1) or j==len(nums2): return 0
            
            # because its subsequence this is logic to find.
            a = nums1[i]*nums2[j] + solve(i+1, j+1)
            b = solve(i+1, j)
            c = solve(i, j+1)
            
            return max(a,b,c)
        
        min_nums1, min_nums2 = min(nums1), min(nums2)
        max_nums1, max_nums2 = max(nums1), max(nums2)
        
        if (min_nums1>0 and max_nums2<0) or (max_nums1<0 and min_nums2>0):
            return max(min_nums1*max_nums2, max_nums1*min_nums2)
        
        return solve(0,0)