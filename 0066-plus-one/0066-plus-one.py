class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        
        done = False
        while n>=0:
            if digits[n]==9:
                digits[n]=0
                n-=1
            else:
                digits[n] = digits[n]+1
                done = True
                break
        
        if not done:
            digits.insert(0, 1)
        
        return digits