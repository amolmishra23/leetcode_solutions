class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        res, carry = deque(), 0
        
        while i>=0 or j>=0:
            if i>=0 and a[i]=="1": carry += 1
            if j>=0 and b[j]=="1": carry += 1
            
            i-=1; j-=1
                
            quo, rem = divmod(carry, 2)
            res.appendleft(str(rem))
            carry = quo
            
        if carry: res.appendleft("1")
                
        return ''.join(res)