class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l, res = 0, float("inf")
        bits = [0]*32
        
        for r in range(len(nums)):
            for i in range(32):
                if nums[r] & (1<<i):
                    bits[i] += 1
            
            curr_val = 0
            for i in range(32):
                if bits[i]:
                    curr_val += (1<<i)
                    
            while l<=r and curr_val >= k:
                res = min(res, r-l+1)
                
                for i in range(32):
                    if nums[l] & (1<<i):
                        bits[i] -= 1
                
                curr_val = 0
                for i in range(32):
                    if bits[i]:
                        curr_val += (1<<i)
                
                l+=1
                        
        return -1 if res==float("inf") else res