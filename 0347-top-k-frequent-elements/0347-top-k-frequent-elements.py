class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-v, k) for k,v in Counter(nums).items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]
        