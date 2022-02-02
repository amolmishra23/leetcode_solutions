class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Problem is to be solved using sliding window. 
        First we get a counter of pattern. And keep count of done chars. 
        Everytime we are at count==0, store the starting of window. 
        Having a count variable, we get rid of iterating over the entire cache dict. 
        And as soon as j-i+1>len(p), we also keep updating the index of i.
        """
        i, j = 0, 0
        cache = Counter(p)
        count = len(cache)
        res = []
        
        for j in range(len(s)):
            if s[j] in cache:
                # decrementing in cache and count. 
                cache[s[j]] -= 1
                if cache[s[j]]==0: count-=1
            if j-i+1>=len(p):
                if count==0: res.append(i)
                # adjustment of the window. 
                if s[i] in cache:
                    if cache[s[i]]==0: count+=1
                    cache[s[i]]+=1
                i+=1
                
        return res
                
            
        
        