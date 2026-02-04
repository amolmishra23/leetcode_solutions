class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")

        # l = window start, p = peak, q = valley
        l = p = q = 0
        window_sum = nums[0]

        for r in range(1, n):
            window_sum += nums[r]

            # Equal neighbors break "strictly inc/dec" immediately.
            # So any trionic subarray must restart after this point.
            if nums[r - 1] == nums[r]:
                l = p = q = r
                window_sum = nums[r]
                continue

            # Case 1: we are moving down at (r-1 -> r)
            if nums[r - 1] > nums[r]:
                # If the step before was moving up, we just flipped inc -> dec,
                # so r-1 is a peak candidate.
                if r > 1 and nums[r - 2] < nums[r - 1]:
                    p = r - 1

                    # When a new decreasing middle begins, the "old last increasing"
                    # (from a previous attempt) becomes the "new first increasing".
                    # That requires the new first increasing to start at l = q,
                    # so we drop everything before q from the window.
                    while l < q:
                        window_sum -= nums[l]
                        l += 1

                    # Optional improvement for maximizing sum:
                    # The first segment nums[l..p] is strictly increasing.
                    # If it starts with negative numbers, dropping them can only help the sum,
                    # and the remaining suffix is still strictly increasing.
                    #
                    # But we must keep at least 2 elements in the first segment:
                    # need l < p  => length >= 2 => l + 1 < p is the safe condition.
                    while l + 1 < p and nums[l] < 0:
                        window_sum -= nums[l]
                        l += 1

            # Case 2: we are moving up at (r-1 -> r)
            else:
                # If the step before was moving down, we just flipped dec -> inc,
                # so r-1 is the valley candidate.
                if r > 1 and nums[r - 2] > nums[r - 1]:
                    q = r - 1

                # If we have valid l < p < q, then nums[l..r] is trionic
                # (we're currently in the last increasing phase).
                if l < p < q:
                    res = max(res, window_sum)

        return res