class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0]*(len(nums)+1)
        
        for n in nums:
            idx = min(len(nums), n)
            count[idx] += 1
            
        right_count = 0
        for i in range(len(nums), -1, -1):
            right_count += count[i]
            if i == right_count: return right_count
            
        return -1