class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        candidates = [None]*len(mat)
        
        for i, row in enumerate(mat):
            candidates[i]=[sum(row), i]
        
        candidates.sort(key=lambda c: (c[0], c[1]))
        
        return [i for _, i in candidates[:k]]
        