class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def has_won(board, player):
            for i in range(3):
                if all([board[i][j]==player for j in range(3)]): return True
                if all([board[j][i]==player for j in range(3)]): return True
                
            return (
                (board[0][0]==board[1][1]==board[2][2]==player) or
                (board[0][2]==board[1][1]==board[2][0]==player)
            )
        
        char_x, char_o = "X", "O"
        count_x, count_o = sum(row.count(char_x) for row in board), sum(row.count(char_o) for row in board)
        if count_o not in set([count_x, count_x-1]): return False
        if has_won(board, char_x) and count_x!=count_o+1: return False
        if has_won(board, char_o) and count_x!=count_o: return False
        return True
                    