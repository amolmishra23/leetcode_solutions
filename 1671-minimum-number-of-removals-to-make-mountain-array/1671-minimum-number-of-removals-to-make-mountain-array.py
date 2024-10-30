class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    lis[i] = max(lis[i], 1+lis[j])
                    
        lds = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], 1+lds[j])
            
        res = n
        for i in range(1, n-1):
            if min(lis[i], lds[i])>1:
                res = min(
                    res, 
                    n - lis[i] - lds[i] + 1
                )
                
        return res