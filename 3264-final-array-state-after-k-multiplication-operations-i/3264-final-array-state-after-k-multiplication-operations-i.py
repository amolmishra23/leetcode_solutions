class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = list(zip(nums, range(len(nums))))
        heapify(heap)

        while k:
            num, idx = heappop(heap)
            heappush(heap,(num * multiplier, idx))
            k-=1

        heap.sort(key = lambda x: x[1])
        
        return list(zip(*heap))[0]