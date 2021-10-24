class Solution:
    """
    The idea is to recursively solve the problem
    Break the string at every possible point, and see if we can find a combination which actually holds this fibonaci property
    """
    def findRec(self, n1, n2, s, found):
        # if we reached end of string and found was True by far
        if s=="" and found: return True
        
        # expected value
        n3 = str(n1+n2)
        
        # comparing if n3 actually exists
        # if it does recursively calling again, to see if we are on right path
        if s[:min(len(n3), len(s))] == n3: return self.findRec(n2, int(n3), s[len(n3):], True)
        
        # else we just return false.
        return False
        
    def isAdditiveNumber(self, nums: str) -> bool:
        # first number size will vary from 1 to n-2. Leaving atleast 1 space for j
        for i in range(1, len(nums)-1):
            n1 = int(nums[:i])
            
            # making sure the number doesnt start with 0. Else we break off. 
            if str(n1) != nums[:i]: break
                
            # second number will go from i+1 to n
            for j in range(i+1, len(nums)):
                
                # 2nd number starts at i
                # goes as long as j we are iterating. 
                n2 = int(nums[i:j])
                
                # same condition as above
                if str(n2) != nums[i:j]: break
                    
                # now making sure, (n1,n2) we chose, actually adding to n3 exist.
                # recursively exist all the way down to the end of string. 
                if self.findRec(n1, n2, nums[j:], False): return True
        
        return False
                
                