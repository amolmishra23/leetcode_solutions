import math

class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        
        # Positions and prefix sums for quick calculations
        positions = [fruit[0] for fruit in fruits]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + fruits[i][1]

        max_fruits = 0
        left = 0
        for right in range(n):
            # Current window of fruits is from index `left` to `right`
            pos_l, pos_r = positions[left], positions[right]
            
            # Calculate the minimum steps to cover the current window [pos_l, pos_r]
            # This is the cost to travel the segment plus the cost to get to the nearer end
            cost = (pos_r - pos_l) + min(abs(startPos - pos_l), abs(startPos - pos_r))

            # If the cost is too high, shrink the window from the left
            while left <= right and cost > k:
                left += 1
                if left > right:
                    break
                # Recalculate cost for the new, smaller window
                pos_l, pos_r = positions[left], positions[right]
                cost = (pos_r - pos_l) + min(abs(startPos - pos_l), abs(startPos - pos_r))

            # If the window is valid, calculate fruits and update max
            if left <= right:
                current_fruits = prefix_sum[right + 1] - prefix_sum[left]
                max_fruits = max(max_fruits, current_fruits)
                
        return max_fruits