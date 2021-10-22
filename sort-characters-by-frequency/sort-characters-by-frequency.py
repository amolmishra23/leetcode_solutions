from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count, res = Counter(s), []
        max_heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(max_heap)
        for _ in range(len(max_heap)):
            value, key = heapq.heappop(max_heap)
            res.append(key*(-value))
        return ''.join(res)