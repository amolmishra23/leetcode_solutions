class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd, even = 0, 0
        
        for x, count in c.items():
            if count%2:
                odd += 1
                even += count-1
            else:
                even += count
        
        if odd: even += 1
        
        return even
        