class Solution:
    def validPalindrome(self, s: str) -> bool:
        def solve(l,r,is_deleted):
            while l<=r:
                if s[l]!=s[r]:
                    if is_deleted: return False
                    return solve(l+1, r, True) or solve(l, r-1, True)
                l+=1
                r-=1
            return True
        
        return solve(0, len(s)-1, False)