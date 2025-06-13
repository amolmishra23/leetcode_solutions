class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def is_possible(diff):
            res, i = 0, 0
            while i<len(nums)-1:
                if nums[i+1]-nums[i] <= diff:
                    res += 1
                    i += 2
                else:
                    i+=1
            return res >= p

        nums.sort()
        return bisect_left(range(nums[-1]-nums[0]+1), True, key=is_possible)
