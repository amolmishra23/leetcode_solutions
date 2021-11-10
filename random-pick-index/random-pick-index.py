class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        # doing it through reservoir sampling
        # every node should have equal chance of being chosen
        # everytime we see a node, we increment count., and then give it a fair chance to be chosen.
        # in the end, whatever stays in res is returned to the user. 
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)