class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(t[:2])*60+int(t[3:]) for t in timePoints])
        minutes.append(minutes[0]+1440)
        return min(b-a for a,b in zip(minutes[:-1], minutes[1:]))