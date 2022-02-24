class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def solve(idx):
          if idx>=len(nums):
            return 0
          
          return max(
            solve(idx+2)+nums[idx],
            solve(idx+1)
          )
        
        return solve(0)