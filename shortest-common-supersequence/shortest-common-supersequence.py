class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Easiest is str1+str2. 
        The idea being the common chars between them is the LCS. We can avoid repeating LCS twice and remaining all chars need to put. 
        First we find the lcs string of both the strings
        then we keep adding the uncommon chars first, fit the lcs in between and finally return the shortest common supersequence
        """
        def lcs(s1, s2):
            m, n = len(s1), len(s2)
            dp = [["" for _ in range(n+1)] for _ in range(m+1)]
            
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=dp[i-1][j-1]+s1[i-1]
                    else:
                        dp[i][j]=max(dp[i-1][j], dp[i][j-1], key=len)
                        
            return dp[-1][-1]
        
        i, j = 0, 0
        res=""
        for x in lcs(str1, str2):
            while x!=str1[i]:
                res+=str1[i]
                i+=1
            while x!=str2[j]:
                res+=str2[j]
                j+=1
            res+=x
            i+=1
            j+=1
            
        return res+str1[i:]+str2[j:]
            