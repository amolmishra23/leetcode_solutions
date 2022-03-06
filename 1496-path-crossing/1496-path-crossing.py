class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirs = {
            "N": (0,1), "S": (0,-1), "E": (1,0), "W": (-1,0) 
        }
        
        curr = [0,0]
        visited = set()
        visited.add(tuple(curr))
        
        for p in path:
            x,y = dirs[p]
            curr[0], curr[1] = curr[0]+x, curr[1]+y
            if tuple(curr) in visited: return True
            visited.add(tuple(curr))
            
        return False