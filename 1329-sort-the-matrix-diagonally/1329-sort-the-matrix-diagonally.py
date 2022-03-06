import collections

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        lookup = collections.defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                lookup[i-j].append(mat[i][j])
        
        for v in lookup.values():
            v.sort()
            
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mat[i][j] = lookup[i-j].pop()
        
        return mat