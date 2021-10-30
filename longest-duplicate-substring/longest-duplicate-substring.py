class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # CONvert each char to int representation
        A = [ord(c) - ord('a') for c in S]
        
        # sufficiently large number for modding against
        mod = 2**63 - 1
        
        def test(L):
            # p is the factor with which, starting number in the window is multiplied with
            # everytime we remove number from sliding window, we multiply with p
            p = (26**L)%mod
            
            # its to add up the numbers from 0 to L range, multiplying with 26
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:L])
            
            # adding cur to seen
            seen = {cur}
            
            # traversing for rem string, to see if hash repeats
            for i in range(L, len(S)):
                # adding new element, and subtracting old element
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                
                # if we have seen it earlier, return its position
                if cur in seen: return i - L + 1
                
                # adding number to our list otherwise
                seen.add(cur)
                
        # doing binary search to find the perfect longest duplicate substring. 
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        
        # once we found the right position, just return
        return S[res:res + lo]