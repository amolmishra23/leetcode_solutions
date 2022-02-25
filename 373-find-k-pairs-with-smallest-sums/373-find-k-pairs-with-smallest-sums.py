import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                curr = nums1[i]+nums2[j]
                
                if len(max_heap)<k:
                    heapq.heappush(max_heap, (-curr, i, j))
                else:
                    if curr>-max_heap[0][0]: break
                    else:
                        heapq.heappop(max_heap)
                        heapq.heappush(max_heap, (-curr, i, j))
        
        res = []
        
        for elem in max_heap:
            res.append([nums1[elem[1]], nums2[elem[2]]])
        
        return res