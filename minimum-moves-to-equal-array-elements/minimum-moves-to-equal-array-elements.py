class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_, res = min(nums), 0
        
        for x in nums: res += x-min_
            
        return res