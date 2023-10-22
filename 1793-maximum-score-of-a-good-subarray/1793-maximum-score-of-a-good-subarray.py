class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        We could choose greedy here, because it is always going to be continuous subarray
        So if we have a min element, it will stay minimum(even in subsequent turns). 
        Not dp like thing. 
        So greedy will just work fine here
        """
        i, j = k-1, k+1
        res = nums[k]
        curr_min, curr_len = res, 1
        
        while i>=0 or j<len(nums):
            opt1 = nums[i] if i>=0 else float("-inf")
            opt2 = nums[j] if j<len(nums) else float("-inf")
            
            if opt1>opt2:
                curr_min = min(curr_min, nums[i])
                curr_len += 1; i-=1
            else:
                curr_min = min(curr_min, nums[j])
                curr_len += 1; j+=1
                
            res = max(res, curr_min * curr_len)
                
        return res
    