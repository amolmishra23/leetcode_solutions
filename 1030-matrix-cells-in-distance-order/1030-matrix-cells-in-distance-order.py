import collections

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """
        Here goal is to return the coordinates sorted.
        To do the same, we keep adding from the center to the queue
        And then perform bfs as long as we are in limits.
        And keep adding it in sorted order in the res array
        """
        res = []
        visited = [[0]*C for _ in range(R)]
        
        q = collections.deque([(r0, c0)])
        visited[r0][c0] = 1
        
        while q:
            a, b = q.popleft()
            res.append([a, b])
            
            if a-1>=0 and not visited[a-1][b]:
                q.append((a-1, b))
                visited[a-1][b]=1
                
            if a+1<R and not visited[a+1][b]:
                q.append((a+1, b))
                visited[a+1][b]=1
            
            if b-1>=0 and not visited[a][b-1]:
                q.append((a, b-1))
                visited[a][b-1]=1
            
            if b+1<C and not visited[a][b+1]:
                q.append((a, b+1))
                visited[a][b+1]=1
        
        return res