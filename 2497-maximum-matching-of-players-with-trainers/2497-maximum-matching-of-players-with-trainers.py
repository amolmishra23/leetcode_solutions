class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(); trainers.sort()
        i, j = 0, 0
        m, n = len(players), len(trainers)
        res = 0

        for i in range(m):
            while j<n and trainers[j]<players[i]: j+=1
            if j<n: res+=1; j+=1
            else: break

        return res
