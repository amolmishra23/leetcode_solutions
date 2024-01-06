class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0]*n*4
        
    def query(self, idx, left, right, qleft, qright):
        if qleft>right or qright<left: return 0
        
        if qleft<=left and right<=qright: return self.arr[idx]
        mid = (left+right)//2
        return self.query(idx*2+1, left, mid, qleft, qright) + \
            self.query(idx*2+2, mid+1, right, qleft, qright)
        
        
    def update(self, idx, left, right, qpos, qval):
        if qpos<left or qpos>right: return 0
        
        if left==right:
            self.arr[idx]=qval;
            return
        
        mid = (left+right)//2
        self.update(idx*2+1, left, mid, qpos, qval)
        self.update(idx*2+2, mid+1, right, qpos, qval)
        self.arr[idx] = self.arr[idx*2+1] + self.arr[idx*2+2]
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segmentTree = SegmentTree(self.n)
        
        for i, num in enumerate(nums):
            self.segmentTree.update(0, 0, self.n-1, i, num)

    def update(self, index: int, val: int) -> None:
        self.segmentTree.update(0, 0, self.n-1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree.query(0, 0, self.n-1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)