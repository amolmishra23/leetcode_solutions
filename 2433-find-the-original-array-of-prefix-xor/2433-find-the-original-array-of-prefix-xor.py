class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        last = pref[0]
        res = [last]
        
        for n in pref[1:]:
            curr = last ^ n
            res.append(curr)
            last ^= curr
        
        return res