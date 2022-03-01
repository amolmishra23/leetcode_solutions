class Solution(object):
    def median(self, nums):
        mid = len(nums)//2
        if len(nums)%2:
            return nums[mid]
        else:
            return (nums[mid]+nums[mid-1])/2
        
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums: return []
        
        arr = sorted(nums[:(k-1)])
        res = []
        
        start, end = 0, k-1
        
        for num in nums[(k-1):]:
            bisect.insort(arr, num)
            res.append(self.median(arr))
            del arr[bisect.bisect_left(arr, nums[start])]
            start += 1
            
        return res