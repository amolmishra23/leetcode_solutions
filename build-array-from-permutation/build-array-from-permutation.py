class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # we have a weird requirement to store both curr number, and nums[curr] number at the same index in array
        # and eventually remove the curr number, and only retain nums[curr] number
        # to do this, the formula we would use is, multiply and divide by N(len of arr)
        # eventually if we divide this by n, only new number would remain. 
        # this algo is called as euclidean division
        
        for i in range(n):
            nums[i] += n*(nums[nums[i]] % n)
            
        for i in range(n):
            nums[i] //= n
            
        return nums