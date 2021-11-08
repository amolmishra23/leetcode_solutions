class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        How many "on" at the end of nth toggle?

        --> "on" or "off" at each position in an array of length n?

        --> toggle even number times will result in "on", toggle odd number times will result in "off"

        --> for position k, the number of toggles is the number of distinct divisors that k has

        --> divisors always come in pair, which means even number of divisors, for example, 12 has (1,12),(2,6),(3,4).

        --> however, Square Number has odd number of divisors, e.g. 25 has 1,25,5

        --> thus, the number of "on", is the number of perfect square number <= n

        math.sqrt(n) because it tells how many perfect squares less than number n. 
        If input is 26, int(sqrt(26)) comes to 5. And 5 perfect quares are 1,2,3,4,5
        """
        return int(math.sqrt(n))