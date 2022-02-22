class Solution:
    def solve(self, nums, a, b, target, res):
        curr_sum = nums[a]+nums[b]
        left = b+1
        right = len(nums)-1
        
        while left<right:
            temp_sum = curr_sum+nums[left]+nums[right]
            if temp_sum == target:
                res.append([nums[a], nums[b], nums[left], nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]: left+=1
                while left<right and nums[right]==nums[right+1]: right-=1
            elif temp_sum>target:
                right-=1
            else:
                left+=1
                
        
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                self.solve(nums, i, j, target, res)
        
        return res