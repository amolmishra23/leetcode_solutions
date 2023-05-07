class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=qW1O1a40-No
        lis = []
        
        for i, x in enumerate(nums):
            if len(lis)==0 or lis[-1]<=x:
                lis.append(x)
                nums[i] = len(lis)
            else:
                idx = bisect_right(lis, x)
                lis[idx] = x
                nums[i] = idx+1
                
        return nums