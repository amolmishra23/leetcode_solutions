class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h*60+m)
            
        minutes.sort()
        diff = lambda a,b: min(b-a, 1440-(b-a))
        res = min(diff(a,b) for a,b in zip(minutes[:-1], minutes[1:]))
        res = min(res, diff(minutes[0], minutes[-1]))

        return res