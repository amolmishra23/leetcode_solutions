class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        we start from top right corner. 
        if we need a smaller elem => move left
        if we need a bigger elem => move down
        if we cant move any further elem doesnt exist in the array. else we have found elem and returned back true. 
        we are able to do in this algo only because, elements in each row and column are sorted
        """
        if matrix is None or len(matrix)==0 or len(matrix[0])==0:
            return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = [0, cols-1]
        
        while col>=0 and row<=rows-1:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False
        
        