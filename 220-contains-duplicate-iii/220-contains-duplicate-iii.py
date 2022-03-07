import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = []
        for i in range(len(nums)):
            if i > k: del SList[bisect.bisect_left(SList, nums[i-k-1])]   
            pos1 = bisect.bisect_left(SList, nums[i] - t)
            pos2 = bisect.bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2: return True
            
            bisect.insort(SList, nums[i])
        
        return False