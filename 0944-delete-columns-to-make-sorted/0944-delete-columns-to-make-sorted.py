class Solution:
    def isSortedColumn(self, col: int, strs: list[str]) -> bool:
        for i in range(1, len(strs)):
            if strs[i][col] < strs[i - 1][col]:
                return False
        return True

    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            if not self.isSortedColumn(i, strs):
                count += 1
        return count