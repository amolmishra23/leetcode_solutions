class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]: return ""
            for j in range(min_len):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
                    
        visit=set()
        stack=set()
        res=[]
        
#         def dfs(c):
#             if c in visit:
#                 return visit[c]
            
#             visit[c]=True
#             for x in graph[c]:
#                 if dfs(x): return True
                
#             visit[c] = False
#             res.append(c)
            
        def dfs2(node):
            if node in visit: return False
            visit.add(node)
            stack.add(node)
            
            for neigh in graph[node]:
                if neigh in stack: return True
                elif neigh not in visit: 
                    if dfs2(neigh): return True
            
            stack.remove(node)
            res.append(node)
            return False
            
        for c in graph:
            if dfs2(c): return ""
            
        return "".join(res[::-1])