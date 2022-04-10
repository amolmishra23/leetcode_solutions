class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stk = []
        prefix = [0]
        
        for num in nums: prefix.append(prefix[-1]+num)
        
        for i, n in enumerate(nums):
            new_start = i
            while stk and stk[-1][1]>n:
                start, val = stk.pop()
                total = prefix[i] - prefix[start]
                res = max(res, val*total)
                new_start = start
            stk.append((new_start, n))
            
        for start, val in stk:
            total = prefix[len(nums)]-prefix[start]
            res = max(res, val*total)
            
        return res %(10**9 + 7)