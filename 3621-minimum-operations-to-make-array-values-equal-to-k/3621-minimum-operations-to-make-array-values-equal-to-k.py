class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = Counter()

        for i in nums:
            if i<k: return -1
            elif i>k: 
                count[i]+=1

        return len(count)