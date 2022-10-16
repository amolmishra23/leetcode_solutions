class Solution:
    @lru_cache(None)
    def solve(self, curr, days):
        if days==1:
            return max(self.job[curr:])
        
        res, tmp = float('inf'), float('-inf')
        
        for j in range(curr, (self.n-days)+1):
            tmp = max(tmp, self.job[j])
            res = min(res, tmp+self.solve(j+1, days-1))
        
        return res
    
    def minDifficulty(self, job: List[int], d: int) -> int:
        if len(job)<d: return -1
        self.job, self.n = job, len(job)
        return self.solve(0, d)