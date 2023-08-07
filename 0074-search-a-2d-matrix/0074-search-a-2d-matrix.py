class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j =0, len(matrix[0])-1
        
        while 0<=i<len(matrix) and 0<=j<len(matrix[0]):
            curr = matrix[i][j]
            if curr==target: return True
            elif curr>target: j-=1
            else: i+=1
                
        return False