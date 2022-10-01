class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Only logic is, we need to record the points
        While iterating. 
        During which maximum upto then changes. We need to record the (x coordinate of change, max height then)
        """
        res, height = [], []
        
        for s, e, h in buildings:
            height.append((s, -h))
            height.append((e, h))
        
        height.sort(key = lambda x: (x[0], x[1]))
        
        heap = [0]
        prev = 0
        
        for p, h in height:
            if h<0:
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapq.heapify(heap)
            
            curr = -heap[0]
            if prev!=curr:
                res.append((p, curr))
                prev = curr
                
        return res