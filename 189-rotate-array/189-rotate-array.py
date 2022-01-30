class Solution:
    def reverse(self, arr, start, end):
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start +=1
            end -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n # to avoid any overflow conditions.  
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)