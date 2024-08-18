class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, seen = [1], set()
        
        for i in range(n):
            curr = heapq.heappop(heap)
            if i==n-1: return curr
            for j in [2,3,5]:
                if curr*j not in seen:
                    heapq.heappush(heap, curr*j)
                    seen.add(curr*j)
                    
        return