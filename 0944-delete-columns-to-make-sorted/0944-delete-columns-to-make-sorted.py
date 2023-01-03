class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        res = 0
        for j in range(n):
            prev = "a"
            for i in range(m):
                if strs[i][j]<prev:
                    res += 1
                    break
                prev = strs[i][j]
        
        return res