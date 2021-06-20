class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heap_, res=[], 0
        
        for cost in costs: heapq.heappush(heap_, cost)
            
        while heap_:
            temp = heapq.heappop(heap_)
            if temp>coins: break
            
            coins-=temp
            res+=1
            
            if coins==0: return res
        
        return res
            
        