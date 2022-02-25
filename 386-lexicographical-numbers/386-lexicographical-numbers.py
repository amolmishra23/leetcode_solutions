class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(k):
            if k<=n:
                res.append(k)
                t = 10*k
                if t<=n:
                    for i in range(10):
                        dfs(t+i)
        
        res = []
        
        for i in range(1, 10):
            dfs(i)
            
        return res