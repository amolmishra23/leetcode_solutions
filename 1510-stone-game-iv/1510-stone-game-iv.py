class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(n):
            # We cannot make any moves from here. 
            if n==0: return False
            
            for i in range(1, math.floor(math.sqrt(n))+1):
                # Lets say we made move of 4, and from below it returns cant make
                # any further moves. We are good to return off True. (Player 1 wins)
                if not dfs(n-(i*i)): return True
            # We have tried all the moves, and everytime player 2 only won. 
            return False
        
        return dfs(n)
            