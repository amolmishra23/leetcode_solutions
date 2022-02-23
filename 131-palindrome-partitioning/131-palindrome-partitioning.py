class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(i, j): #checks if the string s[i to j] is palindrome or not
            while i<j:
                if s[i]!=s[j]: return False
                i+=1
                j-=1
            return True
        
        def palindrome_part(i, parts, curr_part):
            if i == len(s): #if parsed the entire string append the current partition list to answer
                parts.append(list(curr_part))
                return 
            
            for j in range(i, len(s)): #try all strings starting at i and ending at j where j = (i, len(s))
                if is_palindrome(i, j): #if the substring is palindrome then
                    palindrome_part(j+1, parts, curr_part + [s[i:j+1]]) #add substring to temporary substring list repeat the same process from the index after the palindrome substring ends
            
        parts = []
        palindrome_part(0, parts, [])
        return parts