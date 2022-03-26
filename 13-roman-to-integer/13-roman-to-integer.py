class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym_to_val = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000
        }
        
        result = 0
        
        for i in range(len(s)):
            # to handle cases like IV, we will keep traversing
            # when we find V is bigger than I, we need to add 5 and subtract 2. 
            if i>0 and sym_to_val[s[i]] > sym_to_val[s[i-1]]:
                result += sym_to_val[s[i]] - 2*sym_to_val[s[i-1]]
            # else just keep adding them to the result variable
            else:
                result += sym_to_val[s[i]]
                
        return result