class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0: return True
        ip = [x.lower() for x in s if x.isalnum()]
                
        left, right = 0, len(ip)-1
        while left<right:
            if ip[left]==ip[right]:
                left+=1
                right-=1
            else:
                return False
        return True