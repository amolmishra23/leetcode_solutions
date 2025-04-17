class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count, res = defaultdict(list), 0

        for i, num in enumerate(nums):
            for j in count[num]:
                if (i*j) % k == 0:
                    res += 1
            count[num].append(i)

        return res
