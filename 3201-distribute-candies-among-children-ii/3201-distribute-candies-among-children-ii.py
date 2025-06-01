from math import comb

class Solution:
    def distributeCandies(self, candidates: int, limit: int) -> int:
        # If candidates are more than three times the limit, no distribution is possible.
        if candidates > 3 * limit:
            return 0

        # Calculate the total possible distributions without any restrictions
        # This is the number of combinations to distribute `candidates` into 3 boxes
        # (ans is short for answer and represents the total number of distributions)
        total_distributions = comb(candidates + 2, 2)

        # Subtract the distributions that exceed the limit in any box
        # This happens when the number of candidates exceeds the limit
        if candidates > limit:
            total_distributions -= 3 * comb(candidates - limit + 1, 2)

        # Add back the distributions that were subtracted more than once
        # This correction is needed when candidates are twice over the limit,
        # as those would be subtracted twice in the previous step
        if candidates - 2 >= 2 * limit:
            total_distributions += 3 * comb(candidates - 2 * limit, 2)

        # Return the final count of valid distributions
        return total_distributions
