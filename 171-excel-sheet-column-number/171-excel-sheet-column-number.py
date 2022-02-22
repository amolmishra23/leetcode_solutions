class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        
        for char in columnTitle:
            x = ord(char) - ord('A') + 1
            """
            Logic here is similar to converting a binary number back to integer
            Each digit we process and keep multiplying by 2. 
            Similarly here we keep multiplying it with 26. 
            """
            res = res*26 + x
        
        return res