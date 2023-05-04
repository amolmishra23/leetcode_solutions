class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q, d_q = deque(), deque()
        
        for i,c in enumerate(senate):
            r_q.append(i) if c=="R" else d_q.append(i)
        
        while r_q and d_q:
            r_f, d_f = r_q.popleft(), d_q.popleft()
            if r_f<d_f:
                r_q.append(r_f + len(senate))
            else:
                d_q.append(d_f + len(senate))
            
        return "Radiant" if r_q else "Dire"