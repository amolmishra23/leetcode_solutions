class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows = len(M)
        if rows==0: return M
        cols = len(M[0])
        results = []
        
        for r, row in enumerate(M):
            results.append([])
            for c, col in enumerate(row):
                s, count = 0, 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0<=r+dx<rows and 0<=c+dy<cols:
                            s += M[r+dx][c+dy]
                            count += 1
                results[-1].append(s//count)
            
        return results