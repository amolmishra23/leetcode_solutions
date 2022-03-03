class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i==len(nums1) or j==len(nums2):
                return 0

            solve(i+1, j)
            solve(i, j+1)

            if nums1[i]==nums2[j]:
                temp = 1+solve(i+1, j+1)
                self.res = max(self.res, temp)
                return temp

            return 0

        self.res = 0
        solve(0, 0)
        return self.res
