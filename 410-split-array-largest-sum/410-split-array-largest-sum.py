# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
        
#         @lru_cache(None)
#         """
#         The idea is to make all possible m splits in the array
#         And everytime whatever is the maximum sum obtained, we need to return minimum among them. 
#         """
#         def dp(i, m):
#             if i==n: return 0
            
#             if m==0: return float('inf')
            
#             curr_sum, ans = 0, float('inf')
            
#             for j in range(i, n-m+1):
#                 curr_sum += nums[j]
#                 ans = min(ans, max(curr_sum, dp(j+1, m-1)))
            
#             return ans
        
#         return dp(0, m)
                
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canPartition(largestSum):
            groups = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largestSum:
                    groups += 1
                    curSum = num
            return groups <= m

        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canPartition(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans    