class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # if we find longest subarray with sum [sum(nums)-x], we have found our soln. 
        target = sum(nums)-x
        
        # if target is anyways 0, we need to remove all elements from array
        if target==0: return len(nums)
        
        first_idx, curr_sum, res = {0:-1}, 0, -math.inf
        
        # finding the longest subarray with the sum of target
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum-target in first_idx:
                res = max(res, i-first_idx[curr_sum-target])
            
            if curr_sum not in first_idx: first_idx[curr_sum]=i
        
        return -1 if res==-math.inf else len(nums)-res
        