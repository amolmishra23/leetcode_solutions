from sortedcontainers import SortedList

class Solution:
  def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    m, n = len(matrix), len(matrix[0])

    ans = -math.inf

    """
    We add prefix sum row wise also. 
    Doing it in the order [0,1,2,3], [1,2,3], [2,3], [3] rows. 
    """
    for r1 in range(m):
      arr = [0]*n
      # Expanding step by step into all possible subarrays
      for r2 in range(r1, m):
        for c in range(n):
          arr[c] += matrix[r2][c]
        ans = max(ans, self.solve(arr, k))

    return ans
      
  def solve(self, arr, k):
    """
    Logic is, we keep finding the prefix sum. 
    Now we need sum <=k. 
    So what do we subtract from the running prefix sum to get best possible <=k. 
    For this, all the prefix sums we store it in sorted list. 
    Return the max possible answer <= k. 
    """
    prefix_sum = 0
    seen = SortedList([0])
    ans = -math.inf
    for i in range(len(arr)):
      prefix_sum += arr[i]
      prev_sum = self.ceiling(seen, prefix_sum-k)
      if prev_sum!=None:
        ans = max(ans, prefix_sum-prev_sum)
      seen.add(prefix_sum)
    return ans
      
  def ceiling(self, arr, key):
    """
    bisect_left returns the first index where key can be inserted 
    that array will still be sorted. 
    If this index, contains an element, is next bigger element after key. 
    """
    idx = arr.bisect_left(key)
    if idx<len(arr): return arr[idx]
    return None