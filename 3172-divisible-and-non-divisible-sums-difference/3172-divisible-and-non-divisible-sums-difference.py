class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = (n * (n + 1)) // 2  # Sum of first n natural numbers
        last_divisible = (n // m) * m
        if last_divisible == 0:
            divisible_sum = 0
        else:
            count = (last_divisible - m) // m + 1
            divisible_sum = (m + last_divisible) * count // 2
        
        non_divisible_sum = total_sum - divisible_sum
        return non_divisible_sum - divisible_sum
