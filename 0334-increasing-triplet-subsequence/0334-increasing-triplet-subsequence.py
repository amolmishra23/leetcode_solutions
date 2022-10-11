class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a,b,c = [float('inf')]*3
        
        for x in nums:
            # we check for x<=a instead of x<a,
            # because we dont want our triplet to have repeated numbers
            if x<=a: a=x
            elif x<=b: b=x
            # only if we reached here means, its 3rd number in the sequence
            elif x<c: return True
        
        return False