class Solution:
    """
    Given: The Divisor Game as outlined in the problem

Prove: Alice will win if and only if N % 2 == 0

Part 1) If Alice starts with an even number she will always win.

If Alice has an even number, she can always subtract 1, giving Bob an odd number. Odd numbers are not divisible by 2. They are only divisible by odd numbers. Hence Bob must subtract an odd number. Since odd minus odd is even, Bob will always return an even number to Alice. Alice will thus get a smaller even number after each round of play and Bob will get a smaller odd number after each round of play. Eventually Bob will have to play the number 1 and will lose the game since he will have no options.

Part 2) If Alice starts with an odd number she will always lose.

If Alice has an odd number, she has no choice but to subtract an odd number as odd numbers have no even divisors. Thus Bob will get an even number. Now using the argument from Part 1 above, Bob can take this even number and keep giving an odd number back to Alice by subtracting 1. Thus Bob will always get to play even and Alice will always be stuck with an odd number smaller than her previous odd number after each round. Eventually Alice will have to play the number 1 and will lose the game since she will have no options.
    """
    def divisorGame(self, n: int) -> bool:
        return n%2==0