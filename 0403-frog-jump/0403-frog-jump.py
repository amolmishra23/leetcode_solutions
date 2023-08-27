class Solution:
    def canCross(self, stones: List[int]) -> bool:
        possible_jumps = defaultdict(set)
        
        if stones[1]!=1: return False
        
        # problem definitely starts at 1. with 1 jump only we can reach here
        possible_jumps[1].add(1)
        
        # iterating on all the stones
        for i in range(len(stones[1:])):
            # iterating on each stone ka possible jumps
            for j in possible_jumps[stones[i]]:
                # the jump can be -1, 0, +1 from the stone basically
                # but we dont want to jump backwards, so check that and proceed
                for k in range(j-1, j+2):
                    if k>0 and stones[i]+k in stones:
                        # if the jump is on a volid stone, jump there
                        # after jumping we add that as possible_jump in the future stone. 
                        possible_jumps[stones[i]+k].add(k)
            
        # if we were able to jump till the final stone. 
        return len(possible_jumps[stones[-1]])>0
        