class Solution:
    def shift_char(self, c, num):
        char, num = ord(c), num%26
        return chr(char+num) if not char+num>122 else chr(char-(26-num))
        # return chr(ord(c) + (num%26))
    
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        if n==1: return self.shift_char(s[0], shifts[0])
        
        postfix_sum = [0]*n
        postfix_sum[-1] = shifts[-1]
        
        for i in range(n-2, -1, -1):
            postfix_sum[i] += postfix_sum[i+1] + shifts[i]
            
        print(postfix_sum)
        res = [None]*n
        for i in range(n):
            res[i] = self.shift_char(s[i], postfix_sum[i])
            
        return ''.join(res)
        
        