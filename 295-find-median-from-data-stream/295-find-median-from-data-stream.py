import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.max_heap or -self.max_heap[0]>=num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
            
        if len(self.max_heap)>len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap)>len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
            

    def findMedian(self):
        """
        :rtype: float
        """
        max_len= len(self.max_heap)
        min_len= len(self.min_heap)
        
        if max_len==min_len:
            return (-self.max_heap[0]+self.min_heap[0])/2.0
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()