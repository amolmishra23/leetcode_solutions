class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for a in sorted(arr):
            if a in rank:
                continue
            rank[a] = len(rank) + 1
        return list(map(lambda a: rank[a], arr))