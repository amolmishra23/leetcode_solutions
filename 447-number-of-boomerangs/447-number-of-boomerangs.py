class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dis(a, b):
            dx = a[0]-b[0]
            dy = a[1]-b[1]
            return dx*dx+dy*dy

        num = 0
        for p in points:
            cDict = {}
            for q in points:
                d = dis(p, q)
                cDict[d] = cDict.get(d, 0) + 1
            for val in cDict.values(): num += val * (val - 1)
        return num