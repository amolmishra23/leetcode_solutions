class Solution:
    def maxProfit(self, k: int, arr: List[int]) -> int:
        @lru_cache(None)
        def solve(idx, can_buy, k):
          if idx==len(arr) or k==0:
            return 0
          
          if can_buy:
            return max(
              solve(idx+1, False, k) - arr[idx],
              solve(idx+1, True, k)
            )
          else:
            return max(
              solve(idx+1, True, k-1)+arr[idx],
              solve(idx+1, False, k)
            )
          
        return solve(0, True, k)