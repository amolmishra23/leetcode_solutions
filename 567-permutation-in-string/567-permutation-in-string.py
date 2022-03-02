class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        # take a counter of the smaller string
        cache = Counter(s2)
        # keep a count of the counter object
        count = len(cache)
        i = 0
        
        # iterate over the larger string
        for j in range(len(s1)):
            if s1[j] in cache:
                # if char matches in the counter map, reduce its count
                # also reduce one in our count variable
                cache[s1[j]]-=1
                if cache[s1[j]]==0: count-=1
            
            # if sliding window lenght is now limit
            if j-i+1>=len(s2):
                # check if we have count 0, return True
                if count==0: return True
                
                # if matched char, in beginning of the map. remove it
                # also increase count, if it was one of the matched character
                if s1[i] in cache:
                    if cache[s1[i]]==0: count+=1
                    cache[s1[i]] += 1
                    
                # increase length of the sliding window. 
                i+=1
        
        # as we didnt get any valid match, return false
        return False