class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left_product, right_product = [None for _ in range(n)], [None for _ in range(n)]
        res = [None]*n
        left_product[0] = nums[0]
        right_product[-1] = nums[-1]
        
        for i in range(1, n):
            left_product[i] = left_product[i-1]*nums[i]
        
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1]*nums[i]
        
        
        res[0] = right_product[1]
        for i in range(1, n-1):
            res[i] = left_product[i-1]*right_product[i+1]
        res[-1] = left_product[-2]
        
        return res