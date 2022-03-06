# class Solution:
#     def getStrongest(self, arr: List[int], k: int) -> List[int]:
#         arr.sort()
#         m=arr[(len(arr)-1)//2]
#         arr.sort(key=lambda x: (-abs(x-m), -x))
#         return arr[:k]
    
import heapq
class Solution:
    """
    Smart way of solving the problem. 
    We need k biggest values. 
    So, what we do is, till k values we compute and make it a heap.
    For every further value we insert, we popping the min value as well. (its push followed by pop)
    Now in the end, only k values remain in the PQ. Which is our result. 
    """
    
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1)//2]
        pq = [(abs(num - median), num) for num in arr[:k]]
        heapq.heapify(pq)
        for num in arr[k:]:
            item = (abs(num - median), num)
            heapq.heappushpop(pq, item)
        return [item[1] for item in pq]