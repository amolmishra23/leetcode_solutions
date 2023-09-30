class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # We need to combine 2 concepts to solve this problem
        # 1. min_most element before our current index.
        # 2. The smaller numbers on the right (bigger than min_most on the left). We use aditya verma stack logic here. 
        # if we find any combination satsifying this logic, we are done. 
        if len(nums)<3: return False
        
        min_list = [None]*len(nums)
        min_list[0] = nums[0]
        
        for i in range(1, len(nums)):
            min_list[i] = min(min_list[i-1], nums[i-1])
            
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:
                # throw all the useless elements which are even smaller than min_list[j]
                while stack and stack[-1] <= min_list[j]: stack.pop()
                
                if stack and stack[-1] < nums[j]: return True
                
                stack.append(nums[j])
                
        return False
                    