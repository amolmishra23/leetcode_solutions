class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        candidates = [(sum(row), i) for i, row in enumerate(mat)]
        candidates.sort(key = lambda x: (x[0], x[1]))
        return [i for _, i in candidates[:k]]
        