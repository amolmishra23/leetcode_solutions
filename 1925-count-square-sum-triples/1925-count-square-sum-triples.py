class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        # Iterate a from 1 to n
        for a in range(1, n):
            # Iterate b from a + 1 to n
            for b in range(a + 1, n):
                c_squared = a * a + b * b
                c = int(c_squared ** 0.5)
                
                # Check if c is a perfect square and within range
                if c * c == c_squared and c <= n:
                    cnt += 2 # Count both (a, b, c) and (b, a, c)
        return cnt
