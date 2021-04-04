class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        met_dot = met_e = met_digit = False
        
        for i, char in enumerate(s):
            if char in {'+', '-'}:
                if i>0 and s[i-1] not in {'e', 'E'}: return False
            elif char == ".":
                if met_dot or met_e: return False
                met_dot = True
            elif char in {'e', 'E'}:
                if met_e or not met_digit: return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
            
        return met_digit
        