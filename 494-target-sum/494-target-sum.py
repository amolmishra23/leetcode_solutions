class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        The goal is to find all the permutation count, which putting +/- will result in the target sum. 
        """
        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(i+1, s-nums[i]) + findTarget(i+1, s+nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]
        
        cache = {}
        return findTarget(0, S)