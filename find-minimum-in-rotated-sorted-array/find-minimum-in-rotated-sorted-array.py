class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        As its sorted, must to apply binary search
        After applying binary search, everytime keep checking if any break point, where n+1 th elem is bigger than nth elem
        If yes, we return
        Else keep checking which part has bigger chance of having lowest num., as per binary logic. 
        """
        if len(nums)==1: return nums[0]
        
        if nums[0]<nums[-1]: return nums[0]
        
        low, high = 0, len(nums)-1
        
        while low<high:
            mid = low + (high-low)//2
            if nums[mid]>nums[mid+1]: return nums[mid+1]
            elif nums[mid]<nums[mid-1]: return nums[mid]
            elif nums[low]<nums[mid]: low = mid+1
            else: high = mid-1
                
        return -1