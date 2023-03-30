class Solution:
    def __init__(self):
        self.dic = {}
        
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.dic: return self.dic[(s1, s2)]
        
        n, m = len(s1), len(s2)
        
        # if length is different or count is different, def false. 
        if n!=m or Counter(s1)!=Counter(s2):
            self.dic[(s1, s2)]=False
            return False
        
        # if length is <4 it is def scrambled string
        # if both string are same, it is scrambled
        if n<4 or s1==s2:
            self.dic[(s1, s2)]=True
            return True
        
        f = self.isScramble
        
        for i in range(1, n):
            if (f(s1[:i], s2[:i]) and f(s1[i:], s2[i:])) or \
                (f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i])):
                self.dic[(s1, s2)]=True
                return True
            
        self.dic[(s1, s2)]=False
        return False