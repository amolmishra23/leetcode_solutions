class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res, j = [], 0

        for i in range(1, target[-1]+1):
            res.append("Push")
            if i==target[j]:
                j+=1
            else:
                res.append("Pop")

        return res