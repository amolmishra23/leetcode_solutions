class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = defaultdict(int)
        
        for a,b,c in transactions:
            m[a] -= c
            m[b] += c
            
        debt = list(m.values())
        
        def dfs(s):
            while s<len(debt) and debt[s]==0: s+=1
            
            if s==len(debt): return 0
            
            r = float('inf')
            
            # try to settle to all people
            # everytime we settle to one of them randomly, we start dfs from s+1 and add 1 transaction
            # finally we return min nodes traversed in the dfs. 
            for i in range(s+1, len(debt)):
                if debt[s]*debt[i] < 0:
                    debt[i] += debt[s]
                    r = min(r, 1+dfs(s+1))
                    debt[i] -= debt[s]
                    
            return r
        
        return dfs(0)
    