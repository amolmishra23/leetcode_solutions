class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        Solution is using 2 pointer approach.
        Keeping moving the odd, even pointer as far as we can. As far as, numbers are already in correct place.
        When we reached a point they are in wrong place, we then swap odd, even numbers. (That things are now in proper place.)
        """
        i, j = 0, 1
        n = len(nums)
        
        while i<n and j<n:
            while i<n and nums[i]%2==0: i+=2
            while j<n and nums[j]%2==1: j+=2
            # by reaching here means, i is pointing to odd number
            # and j is pointing to even number
            # hence swap them to make them alright. 
            if i<n and j<n: nums[i], nums[j] = nums[j], nums[i]
                
        return nums