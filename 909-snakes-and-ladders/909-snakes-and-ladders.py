class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        need = {1:0}
        q = deque([(1, 0)])
        
        while q:
            pos, steps = q.popleft()
            for i in range(pos+1, pos+7):
                row, col = (i-1)//n, (i-1)%n
                next_val = board[~row][col if row%2==0 else ~col]
                if next_val>0: i = next_val
                if i==n*n: return need[pos]+1
                if i not in need:
                    need[i] = need[pos]+1
                    q.append((i, need[i]))
        
        return -1