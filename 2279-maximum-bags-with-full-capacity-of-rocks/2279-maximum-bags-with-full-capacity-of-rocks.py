class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        heap, res = [], 0
        for i, (c,r) in enumerate(zip(capacity, rocks)):
            if c-r==0:
                res+=1
            else:
                heapq.heappush(heap, [c-r, i])
            
        while additionalRocks and heap:
            rem, idx = heapq.heappop(heap)
            if rem<=additionalRocks:
                res += 1
                additionalRocks -= rem
            else:
                return res
            
        return res