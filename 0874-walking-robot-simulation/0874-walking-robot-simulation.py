class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_dir = 0
        i, j, ans = 0, 0, float("-inf")
        
        obs = set(tuple(o) for o in obstacles)
        
        for comm in commands:
            if comm==-1:
                curr_dir = (curr_dir+1)%4
            elif comm==-2:
                curr_dir = (curr_dir-1)%4
            else:
                x,y = directions[curr_dir]
                
                while comm and (i+x, j+y) not in obs:
                    comm-=1
                    i+=x
                    j+=y
                
                ans = max(ans, i**2 + j**2)
            
        return ans