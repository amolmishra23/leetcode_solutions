class Solution:
    @functools.lru_cache(None)
    def solve(self, i, j):
        if i>=self.m or j>=self.n: return float('inf')
        
        if i==self.m-1 and j==self.n-1: 
          if self.arr[i][j]<=0:
            return -self.arr[i][j]+1
          return 1
        
        go_right = self.solve(i, j+1)
        go_down = self.solve(i+1, j)
        
        min_health = min(go_right, go_down) - self.arr[i][j]
        
        return 1 if min_health<=0 else min_health
        
    def calculateMinimumHP(self, arr: List[List[int]]) -> int:
        if not arr or len(arr)==0 or len(arr[0])==0: return 0
        self.arr = arr
        self.m, self.n = len(arr), len(arr[0])
        
        return self.solve(0, 0)