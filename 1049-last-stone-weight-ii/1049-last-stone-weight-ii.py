class Solution:
    def lastStoneWeightII(self, num: List[int]) -> int:
        """
        Classic problem of 0-1 knapsack 
        In what subsequences can we divide the array, so as to have min possible difference. 
        """
        def can_partition():
          return can_partition_recursive(0, 0, 0)

        @lru_cache(None)
        def can_partition_recursive(currentIndex, sum1, sum2):
          # base check
          if currentIndex == len(num):
            return abs(sum1 - sum2)

          # recursive call after including the number at the currentIndex in the first set
          diff1 = can_partition_recursive(
            currentIndex + 1, sum1 + num[currentIndex], sum2)

          # recursive call after including the number at the currentIndex in the second set
          diff2 = can_partition_recursive(
            currentIndex + 1, sum1, sum2 + num[currentIndex])

          return min(diff1, diff2)
      
        return (can_partition())