class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def magic(r,c):
            values = set()
            
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] in values or not 1<=grid[i][j]<=9:
                        return 0
                    values.add(grid[i][j])
                    
            for i in range(r, r+3):
                curr_sum = 0
                for j in range(c, c+3):
                    curr_sum += grid[i][j]
                if curr_sum!=15: return 0
            
            for j in range(c, c+3):
                curr_sum = 0
                for i in range(r, r+3):
                    curr_sum += grid[i][j]
                if curr_sum!=15: return 0
                
            diag1 = grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]
            diag2 = grid[r+2][c]+grid[r+1][c+1]+grid[r][c+2]
            return diag1==diag2==15
        
        res = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                res += magic(r, c)
                
        return res