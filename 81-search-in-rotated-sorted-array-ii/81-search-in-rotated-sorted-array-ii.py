class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        What makes it complicated is, occurence of a sample case like 3,4,5,3,3,3,3.
        Going by the binary search logic, we dont really know which part to traverse into. 
        If that case occurs, we only crawl linearly.
        Else, we anyways know the property, atleast 1 part has to be sorted. We check if our number falls in that sorted array, and keep progressing in the binary search. 
        """
        l, h = 0, len(nums)-1
        
        while l<=h:
            mid = l + (h-l)//2
            
            if nums[mid]==target: return True
            elif nums[l]==nums[mid]==nums[h]: l+=1; h-=1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]: h = mid-1
                else: l = mid+1
            else:
                if nums[mid]<target<=nums[h]: l=mid+1
                else: h = mid-1
        
        return False
                    