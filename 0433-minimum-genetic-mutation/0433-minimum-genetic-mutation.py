class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q, bank = deque([(start, 0)]), set(bank)
        
        while q:
            curr, level = q.popleft()
            if curr == end: return level
            
            for i in range(len(curr)):
                for c in "ACGT":
                    mutation = curr[:i]+c+curr[i+1:]
                    if mutation in bank:
                        bank.remove(mutation)
                        q.append((mutation, level+1))
            
        return -1