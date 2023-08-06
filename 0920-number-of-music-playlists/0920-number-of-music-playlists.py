class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = (10**9)+7
        @lru_cache(None)
        def solve(currIdx, usedCount):
            # Consider it like a basic combinations problem.
            # if we have to just choose new songs out of 6 songs database it will be 6*5*4*3*2*1
            # where it gets tricky is, after k tries, we can even reuse the song. So that incorportation is below. 
            
            # to account for only cases where we have used all the songs, we have the below base condition. 
            if currIdx == goal: return usedCount==n
            
            # if we are reusing, we have a cooldown of k songs. Hence consider only usedCount-k else 0
            reuseCount = (max(0, usedCount-k) * solve(currIdx+1, usedCount))%MOD
            # if we are using new song, means we have options of n-usedCount.
            newCount = ((n-usedCount) * solve(currIdx+1, usedCount+1))%MOD
            
            # total number of ways. 
            return (reuseCount+newCount) % MOD
        
        return solve(0, 0)