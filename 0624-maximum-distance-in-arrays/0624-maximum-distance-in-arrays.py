class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        high_dist, low_dist = [], []
        
        for i, arr in enumerate(arrays):
            heapq.heappush(high_dist, [max(arr), i])
            heapq.heappush(low_dist, [-min(arr), i])
            
            if len(high_dist)>2: heapq.heappop(high_dist)
            if len(low_dist)>2: heapq.heappop(low_dist)
                
        backup_low, backup_high = heapq.heappop(low_dist), heapq.heappop(high_dist)
        res_low, res_high =  heapq.heappop(low_dist), heapq.heappop(high_dist)
        if res_low[1]!=res_high[1]:
            return res_high[0]+res_low[0]
        
        return max(res_high[0]+backup_low[0], backup_high[0]+res_low[0])