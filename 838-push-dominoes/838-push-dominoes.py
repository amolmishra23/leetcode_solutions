class Solution:
    def pushDominoes(self, d: str) -> str:
        d, q = list(d), deque()
        
        for i,x in enumerate(d): 
            if x!=".": q.append((i, x))
            
        while q:
            i, x = q.popleft()
            
            # if L is still there, and not popped out.
            # means definitely we need to set at (i-1)th index as L. 
            if x=="L" and i>0 and d[i-1]==".":
                d[i-1]="L"
                q.append((i-1, "L"))
            # in case of R, we need to check if there is an adjacent L, beside dot
            # if yes, we can ignore this R presence, and also pop adj L
            # else we just mark the next dot index(i+1) as R
            elif x=="R":
                if i<len(d)-1 and d[i+1]==".":
                    if i<len(d)-2 and d[i+2]=="L":
                        q.popleft()
                    else:
                        d[i+1]="R"
                        q.append((i+1, "R"))
                        
        # after nothing to be processed in queue, we can return this. 
        return "".join(d)

        