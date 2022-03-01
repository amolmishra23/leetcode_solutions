class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1: return False
        
        sum_ = 1
        
        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                sum_ += (i)+(num//i)
                
        return sum_ == num