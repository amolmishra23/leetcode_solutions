class Solution:
    def helper(self, curr, start):
        end = len(self.nums)-1
        
        # here we do binary search logic to quicken our search
        while start<end:
            temp = self.nums[start]+self.nums[end]
            
            # if we found our triplet, there may still be more present
            # apart more being present we also need to mitigate for the repeated entries
            if temp+curr==0:
                self.res.append((curr, self.nums[start], self.nums[end]))
                start += 1
                end -= 1
                while start<end and self.nums[start]==self.nums[start-1]: start+=1
                while start<end and self.nums[end]==self.nums[end+1]: end-=1
            
            # else we move either directions based on the binary search logic. 
            elif temp+curr>0:
                end -= 1
            else:
                start += 1
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        In order to ignore repeated numbers, easiest way is to sort it, and keep comparing to the next number
        """
        self.nums = sorted(nums)
        self.res = []
        
        for i in range(len(self.nums)):
            # if it repeats, we just skip it
            if i>0 and self.nums[i]==self.nums[i-1]: continue
            # else we attempt to search for a triplet summing up to 0
            self.helper(self.nums[i], i+1)
            
        return self.res