class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        return heapq.nsmallest(k, count, key=lambda x: (~count[x], x))