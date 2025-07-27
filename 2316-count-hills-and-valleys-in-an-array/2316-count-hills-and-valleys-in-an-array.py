class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        # Step 1: Remove consecutive duplicates (Data Compression)
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])

        # Step 2: Loop through the filtered array (Sliding Comparison)
        count = 0
        for i in range(1, len(filtered) - 1):
            prev, curr, next_ = filtered[i - 1], filtered[i], filtered[i + 1]

            # Step 3: Check for hills or valleys (Local Minima/Maxima Detection)
            if (curr > prev and curr > next_) or (curr < prev and curr < next_):
                count += 1  # Step 4: Increment the count for hills/valleys (Greedy Counting)

        return count