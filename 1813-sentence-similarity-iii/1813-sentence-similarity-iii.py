class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(" "), sentence2.split(" ")
        
        n1, n2 = len(s1), len(s2)
        if n1>n2:
            s1, s2 = s2, s1
            n1, n2 = n2, n1
            
        r2, r1 = n2-1, n1-1
        while r1>=0:
            if s1[r1]==s2[r2]:
                r1-=1
                r2-=1
            else:
                break
                
        l2, l1 = 0, 0
        while l1<n1:
            if l1==r1+1: 
                return True
            if s1[l1] == s2[l2]:
                l1+=1
                l2+=1
            else:
                break
        
        return l1 >= r1+1