class Solution:
# @return a boolean
    def __init__(self):
        self.dic = {}
        
    def isScramble(self, s1, s2):
        if (s1, s2) in self.dic: return self.dic[(s1, s2)]
        
        n, m = len(s1), len(s2)
        
        if n != m or sorted(s1) != sorted(s2):
            self.dic[(s1, s2)] = False
            return False
        
        if n < 4 or s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        
        f = self.isScramble
        
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                self.dic[(s1, s2)] = True
                return True
        
        self.dic[(s1, s2)] = False
        return False