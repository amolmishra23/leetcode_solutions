class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The concept is that, when we have a sorted array thats rotated. 
        We have 2 arrays in ascending order. 
        We just need to perform search in one of the arrays
        """
        def perform_binary_search(arr, left, right, target):
            while left<=right:
                mid = left+(right-left)//2
                
                if arr[mid]==target: return mid
                elif arr[mid]>target: right=mid-1
                else: left=mid+1
            
            return -1
        
        def find_breakpoint(arr):
            if arr[0]<arr[-1]: return 0
            
            mid = 0
            left, right = 0, len(arr)-1
            
            while left<right:
                mid = left + (right-left)//2
                
                if arr[mid]>arr[mid+1]: return mid
                elif arr[mid-1]>arr[mid]: return mid-1
                elif arr[mid]>arr[0]: left = mid+1
                else: right = mid-1
            
            return mid
        
        bp = find_breakpoint(nums)
        left, right = 0, len(nums)-1
        
        return perform_binary_search(nums, left, bp, target) if nums[left]<=target<=nums[bp] else perform_binary_search(nums, bp+1, right, target)