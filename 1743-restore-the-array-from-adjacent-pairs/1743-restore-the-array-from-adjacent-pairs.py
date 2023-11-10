class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        count, graph = Counter(), defaultdict(list)
        res = []
        
        for x,y in adjacentPairs:
            count[x]+=1; count[y]+=1
            graph[x].append(y)
            graph[y].append(x)
        
        for x,y in count.items():
            if y==1: res = [x, graph[x][0]]
                
        while len(res)<len(adjacentPairs)+1:
            curr, prev = res[-1], res[-2]
            res.append(graph[curr][1] if graph[curr][0]==prev else graph[curr][0])
                
        return res
            