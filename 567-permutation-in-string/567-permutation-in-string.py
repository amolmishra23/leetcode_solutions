class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        cache = Counter(s2)
        count = len(cache)
        i = 0
        
        for j in range(len(s1)):
            if s1[j] in cache:
                cache[s1[j]]-=1
                if cache[s1[j]]==0: count-=1
            
            if j-i+1>=len(s2):
                if count==0: return True
                if s1[i] in cache:
                    if cache[s1[i]]==0: count+=1
                    cache[s1[i]] += 1
                i+=1
        
        return False