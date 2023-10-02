class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, curr_a = 0,0
        b, curr_b = 0, 0
        
        for c in colors:
            if c=="A":
                curr_a += 1
                if curr_a >=3: 
                    a+=1
                curr_b = 0
            else:
                curr_b += 1
                if curr_b >=3:
                    b+=1
                curr_a = 0
                
        return a>b