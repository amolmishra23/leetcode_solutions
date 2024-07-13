class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([[a,b,c,i] for i, (a,b,c) in enumerate(zip(positions, healths, directions))])
        stk = []
        
        for a,b,c,i in robots:
            while stk and stk[-1][2]=="R" and c=="L":
                if stk[-1][1]>b:
                    stk[-1][1]-=1
                    break
                elif stk[-1][1]<b:
                    stk.pop()
                    b-=1
                else:
                    stk.pop()
                    break
            else:
                stk.append([a,b,c,i])
                
        return [y[1] for y in sorted(stk, key = lambda x: x[3])]
                    