class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n, i = len(nums), 0
        
        # doing this in constant place is the tough thing
        while i<n:
            # replacing at correct position. 
            if nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            # if num already exists at that position, just proceed to next index
            else: i+=1
        
        # result of final missing numbers
        missing = []
        
        # if we didnt find i+1, means i+1 is missing
        # append it to missing numbers list
        # return the missing number
        for i in range(len(nums)):
            if nums[i]!=i+1:
                missing.append(i+1)
                
        return missing