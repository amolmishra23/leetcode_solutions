class Solution:
    def winnerOfGame(self, a: str) -> bool:
        a_count, b_count = 0,0
        for i in range(1, len(a)-1):
            if a[i-1]==a[i]==a[i+1]:
                if a[i]=="A":
                    a_count += 1
                else:
                    b_count += 1
        
        return a_count > b_count
        
    def winnerOfGame2(self, colors: str) -> bool:
        """
        logic is to find extra a,b (in the continous streak of 3)
        And figure which has most extra in the end
        """
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