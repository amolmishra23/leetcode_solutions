class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        for word,count in Counter(words).items():
            heapq.heappush(heap, (-count, word))
            
        res = []
        for _ in range(k):
            if not heap: break
            res.append(heapq.heappop(heap)[1])
        
        return res