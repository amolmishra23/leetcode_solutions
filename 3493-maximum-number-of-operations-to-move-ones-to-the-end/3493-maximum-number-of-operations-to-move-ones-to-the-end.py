class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ones = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                # if this zero is the end of its zero-block (next is '1' or this is last char),
                # then every '1' to its left can be moved past this zero once -> add ones.
                if i == n - 1 or s[i + 1] == '1':
                    ans += ones

        return ans
