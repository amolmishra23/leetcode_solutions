class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, h = 0, len(nums)-1
        
        while l<=h:
            mid = l+(h-l)//2
            
            if nums[mid]==target: return True
            elif nums[l]==nums[mid]==nums[h]: l+=1; h-=1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]: h=mid-1
                else: l=mid+1
            else:
                if nums[mid]<target<=nums[h]: l=mid+1
                else: h= mid-1
                    
        return False