class Solution:
    def evenCount(self, num):
        res = 0
        while num:
            num, rem = divmod(num, 10)
            res += 1
        return 1-(res%2)

    def findNumbers(self, nums: List[int]) -> int:
        return sum([self.evenCount(num) for num in nums])