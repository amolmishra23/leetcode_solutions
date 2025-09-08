class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        check = lambda x: '0' not in str(x)

        for i in range(1,n):
            j = n-i
            if check(i) and check(j): return [i,j]