class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        maxi = sum(chalk)
        k %= maxi
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k-=chalk[i]