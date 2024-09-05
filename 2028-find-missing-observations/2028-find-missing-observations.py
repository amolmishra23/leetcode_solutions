class Solution:
    def split(self, target, k):
        if not 1*k <= target <= 6*k: return []
        res = [target//k]*k
        diff = target-sum(res)
        
        for i in range(diff): res[i]+=1
        return res
        
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_count, curr_sum = len(rolls)+n, sum(rolls)
        total_sum = total_count*mean        
        diff_sum = total_sum - curr_sum 
        return self.split(diff_sum, n)
        