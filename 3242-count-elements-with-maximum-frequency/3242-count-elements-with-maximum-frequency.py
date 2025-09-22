class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = max_freq = count.most_common()[0][1]
        
        for el, count in count.most_common()[1:]:
            if count!=max_freq: break 
            res += count

        return res