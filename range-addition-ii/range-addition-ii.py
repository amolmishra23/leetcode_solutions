class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        if len(ops)==0: return m*n
        
        temp, max_, count_ = [[0]*n for _ in range(m)], float('-inf'), m*n
        
        for x, y in ops:
            for i in range(min(x, m)):
                for j in range(min(y, n)):
                    temp[i][j] += 1
                    if temp[i][j]>max_:
                        max_, count_ = temp[i][j], 1
                    elif temp[i][j]==max_:
                        count_ += 1

        return count_
        """
        
        """
        Instead of solving in n**2 way, we can rather solve in 2*n way
        All we care about is, which row and which col, instead of populating the entire matrix
        And in the end, for sure highest value is in row[0], so we see how far that is present
        And we also see highest in col[0], so we see how far that is present
        """
        
        row, col = [0]*m, [0]*n
        
        for x,y in ops:
            for i in range(min(x, m)): row[i]+=1
            for j in range(min(y, n)): col[j]+=1
        
        row_c, col_c = 0, 0
        
        while row_c<m and row[row_c]==row[0]: row_c+=1
        while col_c<n and col[col_c]==col[0]: col_c+=1
            
        return row_c*col_c
        