class Solution:
    def outerTrees(self, points):
        def quater(p):
            x, y = p
            if x >= 0 and y >= 0: return 2
            if x < 0 and y >= 0: return 1
            if x < 0 and y < 0: return 4
            if x >= 0 and y < 0: return 3

        def compare(p1, p2):
            if quater(p1) == quater(p2):
                t1 = p1[1]*p2[0] - p2[1]*p1[0]
                return  1 - 2*int((-p1[1], p1[0]) < (-p2[1], p2[0])) if t1 == 0 else 1 if t1 > 0 else -1
            else:
                return 1 if quater(p1) < quater(p2) else -1
        
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(points)
        points.pop(points.index(start))
        points = [[x - start[0], y - start[1]] for x, y in points]
        points.sort(key = cmp_to_key(compare))

        ans = [[0, 0]]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        
        return [[x + start[0], y + start[1]] for x, y in ans]