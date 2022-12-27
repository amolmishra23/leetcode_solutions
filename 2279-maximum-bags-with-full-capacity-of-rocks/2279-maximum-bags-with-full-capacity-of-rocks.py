class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res, heap = 0, []
        for c, r in zip(capacity, rocks):
            if c-r==0: res += 1
            else: heapq.heappush(heap, c-r)
                
        while additionalRocks and heap:
            rem = heapq.heappop(heap)
            if rem<=additionalRocks:
                res += 1
                additionalRocks -= rem
            else:
                return res
        
        return res