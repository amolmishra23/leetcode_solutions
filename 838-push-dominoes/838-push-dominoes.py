class Solution:
    def pushDominoes(self, d: str) -> str:
        d, q = list(d), deque()
        
        for i,x in enumerate(d): 
            if x!=".": q.append((i, x))
            
        while q:
            i, x = q.popleft()
            
            if x=="L" and i>0 and d[i-1]==".":
                d[i-1]="L"
                q.append((i-1, "L"))
            elif x=="R":
                if i<len(d)-1 and d[i+1]==".":
                    if i<len(d)-2 and d[i+2]=="L":
                        q.popleft()
                    else:
                        d[i+1]="R"
                        q.append((i+1, "R"))
                        
        return "".join(d)

        