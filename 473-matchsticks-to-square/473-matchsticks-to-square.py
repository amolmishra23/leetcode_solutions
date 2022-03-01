class Solution:
    @functools.lru_cache(None)
    def backtrack(self, target_sum, target_part, visited, curr_idx, curr_sum):
        # anyways only one part is left now. So definitely we are successful in splitting it. 
        if target_part==1:
            return True
        
        # successful in making current split. Now 1 less target to make. 
        if curr_sum == target_sum: 
            return self.backtrack(target_sum, target_part-1, visited, 0, 0)
        
        for i in range(curr_idx, len(self.nums)):
            # if number is already visited, or this number is bigger than our target sum just continue
            if visited & (1<<i) or curr_sum+self.nums[i] > target_sum: continue
            
            # adding curr number as visited. 
            visited |= (1<<i)
            
            # checking if our particular step actually resulted in a valid combination. 
            if (self.backtrack(target_sum, target_part, visited, i+1, curr_sum+self.nums[i])): return True
            visited &= ~(1<<i)
            
        return False
    
    def makesquare(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        self.nums = nums
        k = 4
        
        # if these 2 are not possible, soln is also not possible. 
        if len(nums)<k or sum_%k != 0: return False
        
        target, visited = sum_//k, 0
        
        return self.backtrack(target, k, visited, 0, 0)