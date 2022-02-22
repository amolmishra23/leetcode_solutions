class Solution:
    def lps(self, word):
        arr = [None]*(len(word)+1)
        arr[0]=-1
        i, j=0, -1
        while i<len(word):
            while j!=-1 and word[i]!=word[j]: j=arr[j]
            i+=1
            j+=1
            arr[i]=j
            
        return arr
        
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)==0 and len(needle)==0: return 0
        
        temp = needle+"#"+haystack
        n_len = len(needle)
        lps_res = self.lps(temp)[n_len+1:]
        
        for i in range(len(lps_res)):
            if lps_res[i]==n_len:
                return i-n_len
            
        return -1
            