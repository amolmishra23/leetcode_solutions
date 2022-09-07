class Solution:
    
    @lru_cache(None)
    def dp(self, i, k):
        if i==len(self.arr): return 0
        res, local_max = 0, self.arr[i]
        
        for j in range(i,min(i+k, len(self.arr))):
            local_max = max(local_max, self.arr[j])
            res = max(res, local_max*(j-i+1) + self.dp(j+1, k))
        
        return res
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.arr = arr
        return self.dp(0, k)