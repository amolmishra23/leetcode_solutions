class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        count = 0
        i, j = 0, 0
        res = ""
        
        while j<n:
            count = 0
            while j<n and word[i]==word[j] and count<9:
                j+=1
                count += 1
            res += str(count) + word[i]
            i = j
            
        return res