class Solution:
    def backtrack(self, nums, target_sum, target_part, visited, curr_idx, curr_sum):
        if target_part==1:
            return True
        
        if curr_sum == target_sum: 
            return self.backtrack(nums, target_sum, target_part-1, visited, 0, 0)
        
        for i in range(curr_idx, len(nums)):
            if visited[i] or curr_sum+nums[i] > target_sum: continue
            
            visited[i] = True
            if (self.backtrack(nums, target_sum, target_part, visited, i+1, curr_sum+nums[i])): return True
            visited[i] = False
            
        return False
        
        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_ = sum(nums)
        
        if len(nums)<k or sum_%k != 0: return False
        
        target, visited = sum_//k, [False]*len(nums)
        
        return self.backtrack(nums, target, k, visited, 0, 0)