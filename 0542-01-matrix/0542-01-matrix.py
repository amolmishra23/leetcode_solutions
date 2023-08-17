class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dirs = [(1,0), (-1,0), (0, 1), (0,-1)]
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0: q.append((i, j))
                else: mat[i][j]=-1
                    
        while q:
            r, c = q.popleft()
            for i, j in dirs:
                nr, nc = r+i, c+j
                if not 0<=nr<m or not 0<=nc<n or mat[nr][nc]!=-1: continue
                mat[nr][nc] = mat[r][c]+1
                q.append((nr, nc))
        
        return mat
                