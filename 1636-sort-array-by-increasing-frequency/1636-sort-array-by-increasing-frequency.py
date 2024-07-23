class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums).most_common()
        c.sort(key=lambda x: -x[0]); c.sort(key=lambda x: x[1])
        res = []
        for a, b in c:
            res.extend([a]*b)
        return res
