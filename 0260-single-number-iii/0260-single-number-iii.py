class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        We can do it very easily using an extra DS. 
        But to do it efficiently using just 1 DS, is challenging. We use xor to achieve the same. 
        
        XOR of numbers return 1, in case bits at that position are different
        We need to divide numbers in 2 sets, 1 which have a bit set, a bit not set
        If we xor all bit set numbers, we will get only 1 extra number. 
        Same for bits not set
        Hence we get our res with 2 numbers. 
        """
        allxor = 0
        
        for num in nums: allxor ^= num
            
        rightmost_bit = (allxor & (allxor-1))^allxor
        
        res = [0, 0]
        for num in nums:
            if num & rightmost_bit:
                res[0] ^= num
            else:
                res[1]^=num
                
        return res