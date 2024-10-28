class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count, res = Counter(), 0
        
        for n in nums:
            if n*n in count:
                count[n] = count[n*n]+1
            else:
                count[n] = 1
                
            res = max(res, count[n])
            
        return res if res!=1 else -1