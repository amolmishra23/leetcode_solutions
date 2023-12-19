class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[None]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                neigh = [
                    img[ni][nj]
                    for ni in range(i-1, i+2)
                    for nj in range(j-1, j+2)
                    if 0<=ni<m and 0<=nj<n
                ]
                res[i][j] = sum(neigh)//len(neigh)
                
        return res