from collections import deque

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # number cannot start from 0, so start from 1. 
        q = deque(range(1, 10))
        
        # Doing it for n digits/position
        for _ in range(n-1):
            # Each position we try against number of elements carried from prev level
            # Basically both cases. Add k, and subtract k. If it lies within the limit, we add to queue
            for _ in range(len(q)):
                curr = q.popleft()
                if curr%10+k<10: q.append(curr*10 + (curr%10+k))
                if curr%10-k>=0 and k!=0: q.append(curr*10 + (curr%10-k))
        
        return q