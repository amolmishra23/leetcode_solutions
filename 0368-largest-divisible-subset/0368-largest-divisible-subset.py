class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache, res = [[nums[i]] for i in range(len(nums))], []

        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + cache[j]
                    cache[i] = tmp if len(tmp) > len(cache[i]) else cache[i]
            res = cache[i] if len(cache[i]) > len(res) else res

        return res

        # def dfs(i):
        #     if i==len(nums): return []
        #     if i in cache: return cache[i]

        #     res = cache[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j]%nums[i] == 0:
        #             tmp = [nums[i]] + dfs(j)
        #             if len(tmp) > len(res):
        #                 res = tmp

        #     res = cache[i]
        #     return res

        # res = []
        # for i in range(len(nums)):
        #     tmp = dfs(i)
        #     if len(tmp) > len(res):
        #         res = tmp

        # return res