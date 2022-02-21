class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution using moore's algorithm
        
        elem, count = None, 0
        
        for num in nums:
            if count==0:
                elem, count = num, 1
            elif elem==num:
                count += 1
            else:
                count -= 1
                
        return elem if nums.count(elem)>=len(nums)//2 else -1