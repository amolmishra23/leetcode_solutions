class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n, res = len(grid), len(grid[0]), []

        # we need an answer for each column
        for col in range(n):
            curr_col = col
            for curr_row in range(m):
                # next col is either on right or left. Based on value at grid[curr_row][curr_col]
                next_col = curr_col + grid[curr_row][curr_col]
                # checking for not going out of bounds
                # also checking that value in next_col is same. Else we are in loop. 
                if next_col<0 or next_col>=n or grid[curr_row][curr_col]^grid[curr_row][next_col]:
                    curr_col = -1
                    break
                # if all good, we will move to next_row, next_col. Hence update the curr_col for that
                curr_col = next_col
            
            # appending the curr_col for the started col
            res.append(curr_col)
            
        return res