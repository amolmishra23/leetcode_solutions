class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        
        for r, row in enumerate(nums):
            for c, val in enumerate(row):
                if len(res)<=r+c:
                    res.append([])
                res[r+c].append(val)
        
        return [num for row in res for num in reversed(row)]