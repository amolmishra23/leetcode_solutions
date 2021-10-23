class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, mid, high = 0, 0, len(nums)-1
        
        while low<high:
            mid = low + (high-low)//2
            
            if nums[mid] > nums[high]:
                # mid is not the answer
                # smallest number lies between (mid+1) and (high)
                low = mid+1
            elif nums[mid] < nums[high]:
                # mid might be a potential answer
                # but we can now narrow down the search to (low) and (mid)
                high = mid
            else:
                # mid to high is basically useless, as they are equal
                # so we now narrow down 1 step at a time. 
                high -= 1
                
        return nums[low]