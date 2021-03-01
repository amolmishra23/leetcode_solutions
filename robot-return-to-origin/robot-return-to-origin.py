class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir_map = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0)
        }
        
        initial = [0,0]
        
        for char in moves:
            dx, dy = dir_map[char]
            initial[0]+=dx
            initial[1]+=dy
            
        return initial==[0,0]