class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def lps(s):
            arr = [None]*(len(s)+1)
            
            arr[0]=-1
            i, j = 0, -1
            
            while i<len(s):
                while j!=-1 and s[i]!=s[j]: j = arr[j]
                i+=1
                j+=1
                arr[i]=j
                
            return arr
        
        lps_arr = lps(s)
        if lps_arr[-1]==0: return False
        temp = len(s)-lps_arr[-1]
        return len(s)%temp==0 and s[:temp]*(len(s)//temp)==s