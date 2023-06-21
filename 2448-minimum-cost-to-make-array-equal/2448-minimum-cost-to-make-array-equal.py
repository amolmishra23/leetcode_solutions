class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total_count, curr_count = sum(cost), 0
        target = None
        
        for num, c in arr:
            curr_count += c
            if curr_count > total_count//2:
                target = num
                break
        
        return sum(c*abs(num-target) for num,c in arr)