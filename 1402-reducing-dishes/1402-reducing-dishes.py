class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(); n = len(satisfaction)
        total, start = 0, n
        for i in range(n-1, -1, -1):
            total += satisfaction[i]
            if total<0: 
                break
            start-=1
            
        return sum(j*satisfaction[k] for j, k in list(zip(range(1, n+1), range(start, n))))