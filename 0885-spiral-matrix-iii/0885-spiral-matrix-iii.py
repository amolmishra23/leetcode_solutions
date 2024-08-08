class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [(r0,c0)]
        is_valid = lambda x,y: 0<=x<R and 0<=y<C
        
        steps = 1
        r, c = r0, c0
        
        while len(res) < R*C:
            for step in range(steps):
                r,c = r,c+1
                if is_valid(r, c): res.append((r,c))
                
            for step in range(steps):
                r,c = r+1, c
                if is_valid(r, c): res.append((r,c))
                    
            steps += 1
            
            for step in range(steps):
                r,c = r, c-1
                if is_valid(r,c): res.append((r,c))
            
            for step in range(steps):
                r, c = r-1, c
                if is_valid(r,c): res.append((r,c))
                    
            steps += 1
            
        return res