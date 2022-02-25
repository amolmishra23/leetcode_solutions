from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(max_heap)
        res = [heapq.heappop(max_heap)[1] for _ in range(k)]
        return res
            