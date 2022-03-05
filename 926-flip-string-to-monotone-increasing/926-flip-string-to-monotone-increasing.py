class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        start, end = 0, len(s)-1
        
        while start<len(s) and s[start]=="0": start+=1
        
        while end>=0 and s[end]=="1": end-=1
            
        zero_to_one, one_to_zero = 0, 0
        for i in range(start, end+1):
            if s[i]=="0": zero_to_one+=1
            else: one_to_zero+=1
                
            # the idea being if at anytime zero to one, is bigger. We can rather opt to doing one to zero. 
            # the sequence is any no of zeros followed by any number of ones. 
            # For example if input is 100. We rather doing 000, as only 1 op needed.
            if (zero_to_one > one_to_zero):
                zero_to_one = one_to_zero
        
        return zero_to_one