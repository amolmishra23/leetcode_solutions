class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        We know the pattern of LCS so well. But here is LUCS
        The only way to go about is brute force way.
        The biggest string has the best chance to be LUCS. But we need to make sure, if small strings dont make a LCS with it. 
        """
        def is_subsequence(str1, str2):
            # str2 should be bigger length than str1. For str1 to be subsequence of str2. 
            # example: we just need to verify if abc is subsequence of axbxc or not.
            # we travese both the strings, and increment at common chars in str1.
            # if at the end we are at end of str1 means str1 is subsequence of str2
            if len(str1)>len(str2): return False
            
            i = 0
            
            for j in range(len(str2)):
                if i<len(str1) and str1[i]==str2[j]: i+=1
            
            return i==len(str1)
        
        strs.sort(key=len, reverse=True)
        
        for i, word1 in enumerate(strs):
            if all(not is_subsequence(word1, word2) for j, word2 in enumerate(strs) if i!=j): return len(word1)
            
        return -1