class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(key for key, count in Counter(nums).items() if count == 1)