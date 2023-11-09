class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        Logic here is that, we keep moving until we find a homogenous string
        from that totally we can get n*(n+1)/2 substring
        we keep adding it to our res, and keep modding it
        """
        MOD = (10**9)+7
        i, res = 0, 0
        
        natural_sum = lambda x: (x*(x+1))//2
        while i<len(s):
            count, char = 0, s[i]
            while i<len(s) and s[i]==char:
                count += 1; i+=1
            res = (res + natural_sum(count))%MOD
            
        return res