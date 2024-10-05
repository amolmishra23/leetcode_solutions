class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        counter = Counter(s2)
        matched_count = 0
        i = 0
        
        for j in range(len(s1)):
            if s1[j] in counter:
                counter[s1[j]]-=1
                if counter[s1[j]]==0: matched_count +=1 
                    
            if j-i+1 >= len(s2):
                if matched_count == len(counter): return True
                
                if s1[i] in counter:
                    if counter[s1[i]]==0: matched_count-=1
                    counter[s1[i]]+=1
                    
                i+=1
                
        return False
                    