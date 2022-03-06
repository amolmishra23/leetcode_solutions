class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @functools.lru_cache(None)
        def lcs(i, j):
            if i>=len(nums1) or j>=len(nums2): return 0
            if nums1[i]==nums2[j]: return 1+lcs(i+1, j+1)
            return max(lcs(i, j+1), lcs(i+1,j))
        
        return lcs(0,0)