class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(row):
            # filter out all filled elements
            filtered = list(filter(lambda x: x!=".", row))
            # checking if any repeated entry exists
            return len(filtered) == len(set(filtered))
        
        # checking for sanity of all rows and cols
        # they shouldnt contain repeated elements
        for i in range(9):
            if not is_valid_row([board[i][j] for j in range(9)]) or \
                not is_valid_row([board[j][i] for j in range(9)]): return False
            
        # checking for sanity of the 3*3 block
        for i in range(3):
            for j in range(3):
                if is_valid_row([board[m][n] for m in range(3*i, 3*i+3) for n in range(3*j, 3*j+3)]) == False:
                    return False
                
        return True