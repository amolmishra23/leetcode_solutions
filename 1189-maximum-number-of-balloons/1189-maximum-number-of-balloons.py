class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_given, count_expected, res = Counter(text), Counter("balloon"), float('inf')
        for c in count_expected: res = min(res, count_given[c]//count_expected[c])
        return res