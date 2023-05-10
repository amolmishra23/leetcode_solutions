class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0: return []
        if n==1: return [[1]]
        
        matrix = [[0]*n for _ in range(n)]
        counter = 1
    
        rows, cols = n, n
        top, down = 0, rows-1
        left, right = 0, cols-1
        dir = 0
        
        while top<=down and left<=right:
            if dir==0:
                for i in range(left, right+1):
                    matrix[top][i] = counter
                    counter+=1
                top+=1
                
            elif dir==1:
                for i in range(top, down+1):
                    matrix[i][right] = counter
                    counter+=1
                right-=1
                
            elif dir==2:
                for i in range(right, left-1, -1):
                    matrix[down][i] = counter
                    counter += 1
                down-=1
                
            elif dir==3:
                for i in range(down, top-1, -1):
                    matrix[i][left] = counter
                    counter += 1
                left+=1
        
            dir = (dir+1)%4
        
        return matrix