class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        map_={}
        visited = set()
        
        for i, j in zip(s, t):
            if i in map_:
                if map_[i]!=j: return False
            elif j in visited:
                return False
            else:
                map_[i] = j
                visited.add(j)
                
        return True
        