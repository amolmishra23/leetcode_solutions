class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        In this problems we have game with two persons, and we need to understand who is winning, if they play with optimal strategies. In this game at each moment of time we have several (say k) stones, and we say that it is position in our game. At each step, each player can go from one position to another. Let us use classical definitions:

The empty game (the game where there are no moves to be made) is a losing position.
A position is a winning position if at least one of the positions that can be obtained from this position by a single move is a losing position.
A position is a losing position if every position that can be obtained from this position by a single move is a winning position.
Why people use definitions like this? Imagine that we are in winning position, then there exists at least one move to losing position (property 2), so you make it and you force your opponent to be in loosing position. You opponent have no choice to return to winning position, because every position reached from losing position is winning (property 3). So, by following this strategy we can say, that for loosing positions Alice will loose and she will win for all other positions.

So, what we need to check now for position state: all positions, we can reach from it and if at least one of them is False, our position is winning and we can immedietly return True. If all of them are True, our position is loosing, and we return False. Also we return False, if it is our terminal position.


        """
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
            