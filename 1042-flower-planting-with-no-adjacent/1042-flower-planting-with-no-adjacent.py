class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        result = [0]*n
        
        G = defaultdict(list)
        
        for x, y in paths:
            # construct a graph from the given edges
            G[x-1].append(y-1)
            G[y-1].append(x-1)
            
        # whole concept is that, adjacent nodes shouldnt have the same flower
        # so we try to put different flowers across the nodes. 
        for i in range(n):
            result[i] = (
                {1,2,3,4} - 
                {result[j] for j in G[i]}
            ).pop()
        
        return result