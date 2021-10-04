class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<=1: return True
        upper_count = sum([x.isupper() for x in word])
        
        if word[0].isupper() and word[1].isupper(): return upper_count==len(word)
        elif word[0].isupper(): return upper_count==1
        else: return upper_count==0