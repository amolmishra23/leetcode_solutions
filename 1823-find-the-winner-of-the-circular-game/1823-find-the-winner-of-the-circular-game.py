class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def solve(people, sword):
            if len(people)==1: return people[0]
            to_kill = (sword + k)%len(people)
            print("killing...", to_kill)
            people.pop(to_kill)
            print("remaining now...", people)
            return solve(people, (to_kill)%len(people))
        
        k -= 1
        people = list(range(1, n+1))
        return solve(people, 0)
            