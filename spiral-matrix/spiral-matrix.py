class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0: return []
        
        m, n = len(matrix), len(matrix[0])
        
        # right is number of columns
        # bottom is number of rows
        top, bottom = 0, m-1
        left, right = 0, n-1
        res = []
        
        while left<=right and top<=bottom:
            # traversing right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top+=1
            
            # traversing down
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1
            
            # traversing left
            # because condition was only checked at the entry, and might have been messed up by now
            # we could have potentially already traversed the bottom row. 
            if top<=bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
            bottom-=1
            
            # traversing to top
            # because condition was only checked at the entry, and might have been messed up by now
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
            left+=1
            
        return res
            