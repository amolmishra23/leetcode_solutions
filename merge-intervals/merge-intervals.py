class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        res = []
        s1, e1 = intervals[0]
        
        for s2, e2 in intervals:
            if s2<=e1:
                e1 = max(e1, e2)
            else:
                res.append((s1,e1))
                s1 = s2
                e1 = e2
        
        res.append((s1,e1))
        return res
        