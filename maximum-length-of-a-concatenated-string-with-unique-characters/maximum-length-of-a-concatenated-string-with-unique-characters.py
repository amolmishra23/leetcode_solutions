class Solution:
    def maxLength(self, A):
        # declaring an empty set already in dp
        dp = [set()]
        
        for a in A:
            # checking if the current element already has repeated elements
            if len(set(a)) < len(a): continue
            
            # create a set out of curr string
            a = set(a)
            
            # comparing to all prev strings in dp
            for c in dp[:]:
                # if they have any char in common, continue
                if a & c: continue
                # else add all the unique chars in both the strings 
                dp.append(a | c)
        
        # return the longest length string, containing unique characters. 
        return max(len(a) for a in dp)