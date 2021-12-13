class Solution:
    def maxPower(self, s: str) -> int:
        """
        Simple problem to solve using sliding window approach. 
        """
        power = 1
        
        start = 0
        for i in range(1, len(s)):
            if s[start] != s[i]:
                start = i
            power = max(power, i-start+1)
            
        return power