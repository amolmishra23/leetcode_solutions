class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0]*n*4

    def query(self, idx, left, right, qleft, qright):
        if qright<left or qleft>right: return 0
        
        if qleft<=left and right<=qright: return self.arr[idx]
        
        mid = (left+right)//2
        return self.query(2*idx+1, left, mid, qleft, qright) + \
            self.query(2*idx+2, mid+1, right, qleft, qright)
    
    def update(self, idx, left, right, qpos, qval):
        if qpos<left or qpos>right: return
        
        if left==right:
            self.arr[idx]+=1
            return 
        
        mid = (left+right)//2
        self.update(2*idx+1, left, mid, qpos, qval)
        self.update(2*idx+2, mid+1, right, qpos, qval)
        self.arr[idx] = self.arr[2*idx+1]+self.arr[2*idx+2]
        
        
class Solution:
    def compress(self, arr):
        sortedArr = sorted(arr)
        return [bisect.bisect_left(sortedArr, elem) for elem in arr]
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = self.compress(nums)
        segmentTree, res = SegmentTree(n), []
        
        for i, num in enumerate(nums[::-1]):
            res.append(segmentTree.query(0, 0, n-1, 0, num-1))
            segmentTree.update(0, 0, n-1, num, 1)
            
        return res[::-1]