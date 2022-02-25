class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        continuos X are count as single battleship. 
        we need to check if this is part of already counted battleship, or all together a new battleship
        """
        battle_ships = 0
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.': continue
                elif i>0 and board[i-1][j]=='X':
                    continue
                elif j>0 and board[i][j-1]=='X':
                    continue
                battle_ships += 1
        
        return battle_ships