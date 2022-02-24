class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums)==1: 
            self.sum_ = list(nums)
            return
        
        self.sum_ = [0]*len(nums)
        self.sum_[0] = nums[0]
        
        for i in range(1, len(nums)): 
            self.sum_[i] = self.sum_[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if not 0<=left<=right<len(self.sum_): return None
        return self.sum_[right]-(self.sum_[left-1] if left>0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)