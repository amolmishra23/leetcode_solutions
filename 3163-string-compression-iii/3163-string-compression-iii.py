class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        
        i, j, res = 0, 0, ""
        
        while j<n:
            count = 0
            while j<n and word[i]==word[j] and count<9:
                count += 1
                j+=1
            
            res += str(count)+word[i]
            i = j
            
        return res