class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last, n = nums[-1], len(nums)
        res = 0
        
        for i in range(n-2, -1, -1):
            if nums[i] > last:
                k = math.ceil(nums[i]/last)
                # because if 9 is there, i need to split it 2 times. 
                # 9 => 6+3
                # 6 => 3+3
                # hence we make it k-1
                res += (k-1)
                last = nums[i] // k
            else:
                last = nums[i]
            
        return res
            