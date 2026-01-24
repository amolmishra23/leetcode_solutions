class Solution(object):
    def minPairSum(self, nums):
        max_val = float('-inf')
        min_val = float('inf')
        hash_map = [0] * 100001

        for num in nums:
            hash_map[num] += 1
            max_val = max(max_val, num)
            min_val = min(min_val, num)

        low = min_val
        high = max_val
        max_val = float('-inf')
        while low <= high:
            if hash_map[low] == 0:
                low += 1
            elif hash_map[high] == 0:
                high -= 1
            else:
                max_val = max(max_val, low + high)
                hash_map[low] -= 1
                hash_map[high] -= 1

        return max_val
        