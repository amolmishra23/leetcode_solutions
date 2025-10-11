class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def calculate_max_damage(i):
            if i>=len(power):
                return 0

            curr = sortedPower[i]

            # skip current
            duplicates = count[curr]
            skip_index = i+duplicates
            skip_damage = calculate_max_damage(skip_index)

            # include current
            take_damage = curr * count[curr]
            next_index = nextValid[i]
            take_total = take_damage + calculate_max_damage(next_index)

            return max(skip_damage, take_total)

        count = Counter(power)
        sortedPower = sorted(power)

        nextValid = [
            bisect_right(sortedPower, sortedPower[i]+2, lo=i+1, hi=len(power))
            for i in range(len(sortedPower))
        ]

        return calculate_max_damage(0)