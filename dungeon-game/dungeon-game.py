class Solution:
    @functools.lru_cache(None)
    def solve(self, i, j):
        if i>=self.m or j>=self.n: return float('inf')
        
        temp = min(self.solve(i+1, j), self.solve(i, j+1))
        temp = 1 if temp==float('inf') else temp
        
        return max(1, temp-(self.arr[i][j]))
        
    def calculateMinimumHP(self, arr: List[List[int]]) -> int:
        if not arr or len(arr)==0 or len(arr[0])==0: return 0
        self.arr = arr
        self.m, self.n = len(arr), len(arr[0])
        
        return self.solve(0, 0)