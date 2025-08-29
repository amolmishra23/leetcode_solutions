class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Step 1: Count odds and evens in range [1, n]
        oddX = (n + 1) // 2
        evenX = n // 2

        # Step 2: Count odds and evens in range [1, m]
        oddY = (m + 1) // 2
        evenY = m // 2

        # Step 3: Alice wins when x+y is odd
        # Case 1: x odd & y even
        # Case 2: x even & y odd

        # Step 4: Count total winning pairs
        return oddX * evenY + evenX * oddY