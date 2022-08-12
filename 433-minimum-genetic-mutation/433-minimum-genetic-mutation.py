class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        bank = set(bank)
        
        while queue:
            curr, stop = queue.popleft()
            if curr==end: return stop
            for i in range(len(curr)):
                for c in "ACGT":
                    mutation = curr[:i]+c+curr[i+1:]
                    if mutation in bank:
                        bank.remove(mutation)
                        queue.append((mutation, stop+1))
                        
        return -1