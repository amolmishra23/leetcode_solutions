class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = list(map(sum, mat))
        col_sum = list(map(sum, zip(*mat)))
        return sum(mat[i][j]==row_sum[i]==col_sum[j]==1 for i in range(len(mat)) for j in range(len(mat[0])))