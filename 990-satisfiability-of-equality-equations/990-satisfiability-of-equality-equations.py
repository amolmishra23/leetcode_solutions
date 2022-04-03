class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x!=par[x]: par[x] = find(par[x])
            return par[x]
        
        par = {c:c for c in string.ascii_lowercase}
        
        for a,e,_,b in equations:
            if e=="=": par[find(a)] = par[find(b)]
                
        return not any(e=="!" and find(a)==find(b) for a,e,_,b in equations)