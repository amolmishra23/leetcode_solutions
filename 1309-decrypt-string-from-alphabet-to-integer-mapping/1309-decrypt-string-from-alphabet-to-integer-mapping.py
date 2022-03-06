class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict_, count, res, i = {}, 1, [], 0
        
        for x in range(97, 123): dict_[str(count)] = chr(x); count+=1
            
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                res.append(dict_[s[i:i+2]])
                i+=3
            else:
                res.append(dict_[s[i]])
                i+=1
        
        return "".join(res)
                