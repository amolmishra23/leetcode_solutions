class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        catacb
        catacb#bcatac
        0000100012345
        
        basically if we observe catacb, if we just add 1 b in the beginning, it becomes a palindrome.
        Easiest way to find that being, what is the prefix, which is also suffix. 
        If we see catacb#bcatac.
        If we remove the common prefix/suffix, if the remainder we append at the beginning of string.
        b
        it will become bcatacb. Which is a palindrome.         
        """
        def init_arr(w):
            """
            j is the one traversing. 
            i is the one keeping track of the prefix. 
            """
            n, i, j = len(w), 0, 1
            arr = [0]*n
            
            while j<n:
                if w[i]==w[j]:
                    # if prefix is same as the suffix/ 
                    i+=1
                    arr[j]=i
                    j+=1
                elif i==0:
                    # if prefix is not same and we reached end of string. 
                    arr[j]=0
                    j+=1
                else:
                    # we fall back to init_arr, prev index. 
                    i = arr[i-1]
            
            return arr
            
        pal = s+"#"+s[::-1]
        table = init_arr(pal)
        
        return s[table[-1]:][::-1]+s
            