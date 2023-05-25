class Solution:
    def maxScore(self, speed: List[int], efficiency: List[int], k: int) -> int:
        """
        Same as the problem: https://leetcode.com/problems/maximum-performance-of-a-team/
        """
        n = len(speed)
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)
        
        min_heap = []
        
        curr_sum, res = 0, 0
        
        for e,s in engineers:
            # curr_sum stores the sum of top k numbers in sum
            curr_sum += s
            heapq.heappush(min_heap, s)
            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)
                
            # assuming we popped out the s, in prev line. 
            # we ideally dont need to update res. 
            # but no need to worry, because current e is less than previous e. So update wont be there. 
            
            # updating res, with product of curr_sum*e
            if len(min_heap)==k:
                res = max(res, curr_sum*e)
        
        return res