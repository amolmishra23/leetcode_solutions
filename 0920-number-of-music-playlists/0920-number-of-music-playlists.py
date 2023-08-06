class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = (10**9)+7
        @lru_cache(None)
        def solve(currIdx, usedCount):
            if currIdx == goal: return usedCount==n
            
            reuseCount = (max(0, usedCount-k) * solve(currIdx+1, usedCount))%MOD
            newCount = ((n-usedCount) * solve(currIdx+1, usedCount+1))%MOD
            
            return (reuseCount+newCount) % MOD
        
        return solve(0, 0)