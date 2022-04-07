class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Solving using bellman ford algo.
        because we have k stops restriction, it becomes easy to solve using this.
        Every iteration we just keep checking, if by any chance dist to neighbour can become shorter
        Then we make the jump. 
        """
        
        prices = [float('inf')]*n
        prices[src] = 0
        
        for i in range(k+1):
            tmp = list(prices)
            
            for s,d,p in flights:
                if prices[s]==float('inf'): continue
                
                if prices[s]+p<tmp[d]:
                    tmp[d] = prices[s]+p
            
            prices=tmp
            
        return -1 if prices[dst]==float('inf') else prices[dst]