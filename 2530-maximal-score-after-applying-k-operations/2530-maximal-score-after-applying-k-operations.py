class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap, res = [-x for x in nums], 0
        heapq.heapify(heap)
        
        while k:
            elem = -heapq.heappop(heap)
            res += elem
            k-=1
            if ceil(elem/3):
                heapq.heappush(heap, -ceil(elem/3))
                
        return res