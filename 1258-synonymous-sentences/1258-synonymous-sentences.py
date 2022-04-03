class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = {}
        
        def union(x, y):
            uf[find(y)] = find(x)
            
        def find(x):
            uf.setdefault(x, x)
            if uf[x]!=x:
                uf[x] = find(uf[x])
            return uf[x]
        
        for a,b in synonyms:
            union(a, b)
            
        graph = defaultdict(set)
        
        for a,b in synonyms:
            pa = find(a)
            graph[pa] |= set([a,b])
            
        temp = []
        for word in text.split(" "):
            if word in uf:
                temp.append(list(graph[find(word)]))
            else:
                temp.append([word])
                
        return sorted([" ".join(sentence) for sentence in itertools.product(*temp)])