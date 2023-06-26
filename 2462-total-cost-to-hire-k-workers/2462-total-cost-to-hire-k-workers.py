class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        front_heap, back_heap = [], []
        i, j = 0, len(costs)-1
        res = 0
        
        for _ in range(k):
            while len(front_heap)<candidates and i<=j:
                heapq.heappush(front_heap, costs[i])
                i += 1
            
            while len(back_heap)<candidates and i<=j:
                heapq.heappush(back_heap, costs[j])
                j -= 1
                
            a = front_heap[0] if front_heap else float("inf")
            b = back_heap[0] if back_heap else float("inf")
            
            if a<=b:
                res += heapq.heappop(front_heap)
            else:
                res += heapq.heappop(back_heap)
                
        return res
        