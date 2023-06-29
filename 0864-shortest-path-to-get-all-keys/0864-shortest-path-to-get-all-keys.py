class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        We need to visit a node in graph multiple times here
        Because we might need to traverse multiple ways to get the key, before passing the lock
        Hence our visited should contain coordinates and keys by far. 
        Once we have all the keys, we can return the iteration we are in 
        (That being best path to achieve our answer). 
        """
        m, n = len(grid), len(grid[0])
        
        key_count, start = 0, None
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    key_count += 1
                elif grid[i][j] == "@":
                    start = (i, j)
                    
        q, visited = deque(), set()
        q.append((*start, ""))
        distance = 0
        
        while q:
            for _ in range(len(q)):
                i, j, keys = q.popleft()
                if (i,j, keys) in visited: continue

                if len(keys)==key_count: return distance
                visited.add((i, j, keys))

                for di, dj in directions:
                    ni, nj = i+di, j+dj

                    if 0<=ni<m and 0<=nj<n and grid[ni][nj] != "#":
                        curr_val = grid[ni][nj]

                        if curr_val in ".@":
                            q.append((ni, nj, keys))
                        elif curr_val in "abcdef":
                            q.append((ni, nj, keys+curr_val if curr_val not in keys else keys))
                        elif curr_val in "ABCDEF" and curr_val.lower() in keys:
                            q.append((ni, nj, keys))
            
            distance += 1
            
        return -1