class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = {}
        
        def find(x):
            uf.setdefault(x, x)
            if uf[x]!=x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x,y):
            px,py = find(x), find(y)
            if px==py: return False
            uf[px]=py
            return True
        
        for x,y in pairs:
            union(x,y)
            
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[find(i)].append(s[i])
            
        for key in dic:
            dic[key].sort(reverse=True)
            
        res = []
        for i in range(len(s)):
            res.append(dic[find(i)].pop())

        return "".join(res)