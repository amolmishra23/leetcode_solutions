class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = nums.count(1)
        if count_ones > 0: return n-count_ones

        overall_gcd = 0
        for x in nums:
            overall_gcd = math.gcd(overall_gcd, x)

        if overall_gcd > 1: return -1

        min_subarray_length = n+1

        for i in range(n):
            current_gcd = 0

            for j in range(i, n):
                current_gcd = math.gcd(current_gcd, nums[j])

                if current_gcd == 1:
                    length = j-i+1
                    min_subarray_length = min(min_subarray_length, length)
                    break

        if min_subarray_length > n: return -1

        return min_subarray_length + n - 2