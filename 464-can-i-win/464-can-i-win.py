class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}
        
        def can_win(choices, total):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1]>=total: return True

            # if we have seen this exact scenario play out, then we know the outcome
            if tuple(choices) in seen: return seen[tuple(choices)]
            
            # we haven't won yet.. it's the next player's turn.
            # Hoping the next player to loose. Hence check for !can_win. 
            for idx in range(len(choices)):
                if not can_win(
                    choices[:idx]+choices[idx+1:], total-choices[idx]
                ):
                    seen[tuple(choices)] = True
                    return True
                
            # uh-oh if we got here then next player won all permutations, we can't force their hand
            # actually, they were able to force our hand :(
            seen[tuple(choices)]=False
            return False
        
        # let's do some quick checks before we journey through the tree of permutations
        total_sum = (maxChoosableInteger * (maxChoosableInteger+1))/2
        
        # if all the choices added up are less then the total, no-one can win
        if total_sum < desiredTotal: return False 
        
        # if the sum matches desiredTotal exactly then you win if there's an odd number of turns
        if total_sum == desiredTotal: return maxChoosableInteger%2
        
        choices = list(range(1, maxChoosableInteger+1))
        return can_win(choices, desiredTotal)