class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner, loser = Counter(), Counter()
        for i, j in matches: 
            winner[i]+=1
            loser[j]+=1
            
        winners = set(winner).difference(set(loser))
        losers = [k for k,v in loser.items() if v==1]
        return sorted(list(winners)), sorted(losers)