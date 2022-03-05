class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first, last = 0, len(nums)-1
        res = []
        
        while first<=last:
            a = nums[first]**2
            b = nums[last]**2
            
            if a>b:
                res.append(a)
                first += 1
            else:
                res.append(b)
                last -= 1
                
        return res[::-1]