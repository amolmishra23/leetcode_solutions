class Solution:
    # Inspired by Aditya Verma's approach to solve this question! 
    def __init__(self):
        self.dic = {}
        
    def isScramble(self, s1, s2):
        # As its top-down DP, checking if we encountered the same input
        if (s1, s2) in self.dic: return self.dic[(s1, s2)]
        
        n, m = len(s1), len(s2)
        
        # If string lengths are different, or contain different characters, surely not scrambled. 
        if n != m or Counter(s1) != Counter(s2):
            self.dic[(s1, s2)] = False
            return False
        
        # if string length is less than 4, and contain same chars they are scrambled
        if n < 4 or s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        
        f = self.isScramble
        
        # All that matters is, breaking at the right point. 
        # And checking if any condition is satified. 
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                self.dic[(s1, s2)] = True
                return True
        
        self.dic[(s1, s2)] = False
        return False