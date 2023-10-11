class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """
        Lets have the events like 
        0: bloom
        1: person
        2: die
        """
        heap = []
        
        for i,p in enumerate(people):
            heapq.heappush(heap, [p, 1, i])
            
        for i,j in flowers:
            heapq.heappush(heap, [i, 0])
            heapq.heappush(heap, [j, 2])
            
        curr_count = 0
        res = [None]*len(people)
        while heap:
            curr = heapq.heappop(heap)
            
            if curr[1]==0:
                curr_count += 1
            elif curr[1]==2:
                curr_count -= 1
            else:
                res[curr[2]] = curr_count
                
        return res