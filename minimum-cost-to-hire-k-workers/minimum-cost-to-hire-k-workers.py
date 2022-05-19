class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        For all the works, we first find profit. wage/quality.
        Now the intent is, we pick up people based on lowest ratio. 
        
        [[2.5, 20], [6.0, 5], [7.0, 10]]
        add -20 to heap.
        add -5 to heap too. 
        total quality is now 25
        now because we are in k size heap. 25*6 = 150. One of the probable answers. 
        
        Next time, we have new person need to remove their quality. And add curr person quality, and multiply by his ratio. 
        So now total quality becomes 25-20+10 = 15. 15*7=105. More profitable.        
        """
        workers = [[w/q, q] for q, w in zip(quality, wage)]
        workers.sort()  # sort in increasing order by ratio
        print(workers)
        
        maxHeap = []
        totalQuality = 0
        minCost = math.inf
        for r, q in workers:
            heappush(maxHeap, -q)
            totalQuality += q
            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)
            if len(maxHeap) == k:
                print(totalQuality * r)
                minCost = min(minCost, totalQuality * r)
        return minCost