import collections
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                # finding which row and col will it lie in
                # we do i-1, because the indexing starts from 0
                a, b = (i - 1) // n, (i - 1) % n
                
                # if even we can go from left to right
                # if odd, we need to come from right to left
                nxt = board[~a][b if a % 2 == 0 else ~b]
                
                # if its -1, we can give it a skip
                if nxt > 0: i = nxt
                    
                # we reached the destination
                if i == n * n: return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1