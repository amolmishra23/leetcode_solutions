class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        A very smart way to solve the problem. 
        Maintain 2 parallel data structures, to record moves of each player separately. 
        As soon as we reach count of 3. We return a player wins.
        
        Player 1 or 2, to win, basically need to make a continous row or continuous column.
        So have 2 rows, 1 for each player. 2 columns, 1 for each player. 
        And 1 of each forward and backward diagonal. 
        We keep incrementing the ith row and jth col, as we find a move. Similarly for relevant diagonal. 
        As soon as we find count 3, in ith or jth players data structures, they have won the game respectively. 
        """
        # each row, col object for each player. hence multiplied by 2.
        row = [[0]*3, [0]*3]
        col = [[0]*3, [0]*3]
        # each diag object for each player.
        diag = [0]*2
        anti_diag = [0]*2
        
        # player
        # can keep changing 0,1 in iterations. denoting 2 players. 
        p = 0
        
        for r, c in moves:
            row[p][r] += 1
            col[p][c] += 1
            # to check if it belongs to one of the diagonals. 
            diag[p] += (r==c)
            anti_diag[p] += (r+c==2)
            
            # as soon as one of row/col/diag reaches count of 3.
            # we have found the winner and return the value. 
            if 3 in set([row[p][r], col[p][c], diag[p], anti_diag[p]]):
                return "A" if p==0 else "B"
            
            # to change between players, as per iterations. 
            p ^= 1
            
        return "Draw" if len(moves)==9 else "Pending"