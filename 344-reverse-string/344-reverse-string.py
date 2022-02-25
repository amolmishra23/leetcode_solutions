class Solution:
    def reverseString(self, st: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s, e = 0, len(st)-1
        
        while s<e:
            st[s],st[e] = st[e],st[s]
            s+=1
            e-=1