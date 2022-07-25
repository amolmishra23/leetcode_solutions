class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurence(arr, target):
            left, right = 0, len(arr)-1
            res = -1
            
            while left<=right:
                mid = left + (right-left)//2
                if arr[mid]==target:
                    res = mid
                    right = mid-1
                elif arr[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
                    
            return res
        
        def last_occurence(arr, target):
            left, right = 0, len(arr)-1
            res = -1
            
            while left<=right:
                mid = left + (right-left)//2
                if arr[mid]==target:
                    res = mid
                    left = mid+1
                elif arr[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
                    
            return res
        
        return [first_occurence(nums, target), last_occurence(nums, target)]