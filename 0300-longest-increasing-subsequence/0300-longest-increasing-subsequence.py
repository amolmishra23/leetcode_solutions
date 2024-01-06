class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0]*4*n
        
    def query(self, idx, start, end, qleft, qright):
        if qleft>end or qright<start: return 0
        
        if qleft<=start and end<=qright: return self.arr[idx]
        
        mid = (start+end)//2
        left = self.query(2*idx+1, start, mid, qleft, qright)
        right = self.query(2*idx+2, mid+1, end, qleft, qright)
        return max(left, right)
    
    def update(self, idx, start, end, qpos, qval):
        if qpos<start or qpos>end: return 
        
        if start==end:
            self.arr[idx]=qval
            return 
        
        mid = (start+end)//2
        self.update(2*idx+1, start, mid, qpos, qval)
        self.update(2*idx+2, mid+1, end, qpos, qval)
        self.arr[idx] = max(self.arr[idx*2+1], self.arr[idx*2+2])
        
        
class Solution:
    def compressArr(self, arr):
        sortedArr = sorted(arr)
        return [bisect.bisect_left(sortedArr, x) for x in arr]        
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = self.compressArr(nums)
        n = len(nums)
        segmentTree = SegmentTree(n)
        
        for x in nums:
            curr = segmentTree.query(0, 0, n-1, 0, x-1)
            segmentTree.update(0, 0, n-1, x, curr+1)
            
        return segmentTree.query(0, 0, n-1, 0, n-1)