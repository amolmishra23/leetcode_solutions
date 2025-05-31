class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dist, queue = {1:0}, [1]

        for x in queue:
            for i in range(x+1, x+7):
                a, b = (i-1)//n, (i-1)%n
                elem = board[~a][b if a%2==0 else ~b]
                if elem>0: i=elem
                if i==n*n: return dist[x]+1
                if i not in dist:
                    dist[i] = dist[x]+1
                    queue.append(i)

        return -1