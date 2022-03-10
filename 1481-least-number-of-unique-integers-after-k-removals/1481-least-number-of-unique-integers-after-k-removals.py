import heapq
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        heap = []
        
        for elem, freq in count.items():
            heapq.heappush(heap, (freq, elem))
        num_unique = len(count)
        
        while heap and k:
            freq, elem = heapq.heappop(heap)
            if freq<=k:
                k -= freq
                num_unique -= 1
            else:
                break
        
        return num_unique
        