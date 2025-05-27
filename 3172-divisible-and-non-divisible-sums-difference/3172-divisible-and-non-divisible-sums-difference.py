class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = (n * (n + 1)) // 2  # Sum of first n natural numbers

        x = m

        while x<=n:
            total_sum -= 2*x
            x += m

        return total_sum