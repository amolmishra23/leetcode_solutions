class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                
                curr_sum = nums1[i] + nums2[j]
                
                if len(max_heap)<k:
                    heapq.heappush(max_heap, (-curr_sum, i, j))
                else:
                    if curr_sum>-max_heap[0][0]: break
                    else:
                        heapq.heappop(max_heap)
                        heapq.heappush(max_heap, (-curr_sum, i, j))
        
        return [[nums1[i],nums2[j]] for _,i,j in max_heap]