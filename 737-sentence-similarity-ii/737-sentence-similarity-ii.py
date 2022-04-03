class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        uf = {}
        
        def find(x):
            if x not in uf: uf[x]=x
            if x!=uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return False
            uf[px] = py
            return True
        
        if len(sentence1)!=len(sentence2): return False
        
        for x, y in similarPairs:
            union(x, y)
            
        for x, y in zip(sentence1, sentence2):
            if find(x)!=find(y): return False
            
        return True