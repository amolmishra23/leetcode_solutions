class Solution:
    """
    Because pairs are only created if nums[i] == nums[j] and i < j, we can infer a arithmethic sequence from this condition.

A hint was also given from the examples:
[1,1,1,1] have 6 combination
The first 1 have 3 pairs
The second 1 have 2 pairs
The third 1 have 1 pairs
Hence for 4 of 1's, we can have 3 + 2 + 1 combination

Then we just have to store every value count and then count arithmetic sequence sum from 1 to n, given n is the number of appearance for each number.

Please star it if you like my solution and explanation :), any advice or correction would be appreciated.

Thanks !
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for num in d:
            val = d[num]
            for i in range(val):
                pairs += i
        return pairs