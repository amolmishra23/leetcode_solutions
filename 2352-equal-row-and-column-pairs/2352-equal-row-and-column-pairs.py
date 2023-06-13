class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[tuple(row)] += 1
        
        for col in zip(*grid):
            cnt += m[tuple(col)]
            
        return cnt