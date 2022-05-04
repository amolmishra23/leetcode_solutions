class Solution(object):
    def maxOperations(self, nums, k):
        res = 0
        prev = defaultdict(int)
        for num in nums:
            target = k - num
            if prev[target] > 0:
                res += 1
                prev[target] -= 1
            else:
                prev[num] += 1
        return res