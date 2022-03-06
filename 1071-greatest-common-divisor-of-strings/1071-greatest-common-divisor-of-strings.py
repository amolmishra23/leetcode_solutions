class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        ABC + ABCDEF != ABCABCDEF
        ABCABC + ABC == ABCABCABC
        ABABAB + AB == ABABABAB
        
        So good way to check if answer is possible
        """
        if str1+str2 != str2+str1: return ""
        
        if str1==str2: return str1
        
        n1, n2 = len(str1), len(str2)
        x = gcd(n1,n2)
        if str1[:x] == str2[:x]: return str1[:x]
        else: return ""