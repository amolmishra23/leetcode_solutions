class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        Alternate approach to natural numbers sum
        We can also keep adding as we find the same char as prev
        and keep updating our total
        if we have aaa
        a=3
        aa=2
        aaa=1
        
        if we are iterating on substring, its equivalent to adding up 1+2+3 (curr substring count)
        hence we can easily find it out
        else we keep adding just 1 to our answer
        """
        total = 0
        count = 0

        for i in range(len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            total += count
            
        return total % (10**9+7)
        
    def countHomogenous2(self, s: str) -> int:
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