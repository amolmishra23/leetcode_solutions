class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        The idea is, we first make the entire array even.
        If we find any odd numbers, first multiply it by 2. 
        
        Now, deviation means diff between max and min numbers. 
        So find the min number in array, and keep finding max from a max_heap. And keep updating the deviation
        
        Everytime we find max number, try to reduce it by half. 
        When our max number is odd, we cant reduce it by half. And thats our breakpoint. 
        """
        heap, min_ele = [], float('inf')
        
        for x in nums:
            temp = x
            if x%2:
                temp = x*2
            heapq.heappush(heap, -temp)
            min_ele = min(min_ele, temp)
            
        min_diff = float('inf')
        
        while heap[0]%2==0:
            top = -heapq.heappop(heap)
            min_diff = min(min_diff, top-min_ele)
            min_ele = min(min_ele, top//2)
            heapq.heappush(heap, -top//2)
            
        return min(min_diff, -heap[0]-min_ele)
        