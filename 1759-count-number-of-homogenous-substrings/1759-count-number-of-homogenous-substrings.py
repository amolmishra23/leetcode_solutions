class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = (10**9)+7
        i, res = 0, 0
        
        natural_sum = lambda x: (x*(x+1))//2
        while i<len(s):
            count, char = 0, s[i]
            while i<len(s) and s[i]==char:
                count += 1; i+=1
            res = (res + natural_sum(count))%MOD
            
        return res