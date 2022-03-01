class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        res = set()       
        self.dfs(nums, 0, [], res)

        return list(res)

    def dfs(self, nums, start, path, res):
        if len(path) >= 2:
            res.add(tuple(path))

        for i in range(start, len(nums)):
            if not path or path[-1] <= nums[i]:
                path.append(nums[i])
                self.dfs(nums, i + 1, path, res)
                path.remove(path[-1])