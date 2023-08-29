class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Whole intuition is of prefix sum
        At any point when we close the shop, all that matters is:
        1. Number of times no customer visited us, before idx
        2. Number of times customer visited us, after idx
        
        This info we can store in prefix sum way
        And just use it to compute penalty at every idx. 
        And finally return the best idx
        """
        N = len(customers)
        # for prefix sum to work
        # at idx 0, number of times no customer visited us, before idx => 0
        # at idx -1, Number of times customer visited us, after idx => 0
        y, n = deque([0]), deque([0])
        
        for i in range(N):
            y.appendleft(y[0]+int(customers[N-1-i]=="Y"))
            n.append(n[-1]+int(customers[i]=="N"))
        
        min_penalty, idx = float("inf"), -1
        for i in range(N+1):
            penalty = y[i] + n[i]
            if penalty<min_penalty:
                min_penalty = penalty
                idx = i
                
        return idx