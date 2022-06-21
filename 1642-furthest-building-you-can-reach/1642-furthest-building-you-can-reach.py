class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        # we use ladders to max extent. 
        # when out of ladders, start using bricks through min-heap, for min consumption
        # when out of bricks also, return the index. thats the max extent we can reach
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff>0:
                heapq.heappush(heap, diff)
            if len(heap)>ladders:
                bricks -= heapq.heappop(heap)
            if bricks<0:
                return i
            
        return len(heights)-1