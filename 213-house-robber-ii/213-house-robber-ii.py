class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        self.d1 = {}
        self.d2 = {}
        return max(self.helper(nums[:-1],0,1),self.helper(nums[1:],0,2))
    
    def helper(self,arr,pos,arr_type):
        if pos > len(arr) - 1:
            return 0
        if arr_type == 1:
            if pos in self.d1:
                return self.d1[pos]
            self.d1[pos] = max(arr[pos] + self.helper(arr,pos + 2,1),self.helper(arr,pos + 1,1))
            return self.d1[pos]
        else:
            if pos in self.d2:
                return self.d2[pos]
            self.d2[pos] = max(arr[pos] + self.helper(arr,pos + 2,2),self.helper(arr,pos + 1,2))
            return self.d2[pos]
