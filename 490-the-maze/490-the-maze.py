class Solution:
    def hasPath(self, maze, start, destination):
        m, n, stopped = len(maze), len(maze[0]), set()
        def dfs(x, y):
            """
            Whole intent of the problem is, we need to go from start to dest
            If we choose particular direction, we can keep travelling in it endlessly till we hit a wall (1)
            when we hit a wall again we can basically do dfs, which keeps choosing all the 4 paths
            this game is played till we reach destination and return true. 
            else all other invocations keep returning false. 
            """
            if (x, y) in stopped: 
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in (-1, 0) , (1, 0), (0, -1), (0, 1):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY):
                    return True
            return False
        return dfs(*start)