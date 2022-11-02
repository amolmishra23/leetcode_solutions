class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j, res = 0, 0, []
        
        while i<m or j<n:
            if i<m: res.append(word1[i]); i+=1
            if j<n: res.append(word2[j]); j+=1
        
        return "".join(res)
        