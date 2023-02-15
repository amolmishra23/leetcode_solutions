class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res, carry = [], k
        
        while num or carry:
            temp = (num.pop() if num else 0) + (carry%10)
            res.append(temp%10)
            carry = carry//10 + temp//10
            
        return res[::-1]