class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # res = []
        # for num in nums:
        #     temp = 0
        #     while num:
        #         temp += 1
        #         num //= 10
        #     res.append(temp)
        # return sum(r%2==0 for r in res)
        return sum(len(str(n)) % 2 == 0 for n in nums)