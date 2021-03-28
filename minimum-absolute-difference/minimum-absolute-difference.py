class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res, min_ = [], float('inf')
        
        for a,b in zip(arr, arr[1:]):
            if b-a<min_:
                min_ = b-a
                res = [[a, b]]
            elif b-a==min_:
                res.append([a,b])
        
        return res