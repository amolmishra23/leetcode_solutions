import heapq

class KthLargest:        
    def __init__(self, k: int, nums: List[int]):
        self.k, self.k_nums = k, []
        for num in nums: self.add(num)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.k_nums, val)
        if len(self.k_nums)>self.k: heapq.heappop(self.k_nums)
        return self.k_nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)