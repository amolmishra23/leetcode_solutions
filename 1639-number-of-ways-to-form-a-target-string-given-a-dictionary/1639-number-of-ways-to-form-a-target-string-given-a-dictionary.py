class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        # For each column, we need to find counter of characters. 
        count = [[0]*len(words[0]) for _ in range(128)]
        
        for word in words:
            # counting occurences of char, in a particular column!!! 
            for i,c in enumerate(word):
                count[ord(c)][i] += 1
        
        # Dealing with column k, and i is the index in target array
        @lru_cache(None)
        def dp(k, i):
            # if we reached to end of target array, its valid solution
            if i==len(target): return 1
            
            # if we travelled all columns, and not reached target, its invalid solution
            if k==len(words[0]): return 0
            
            # our current target char is target[i]
            c = target[i]
            
            # Skipping the current kth column totally.
            ans = dp(k+1, i)
            
            # We can use kth column only if it has the target character
            if count[ord(c)][k] > 0:
                # multiply the val of count[ord[c]][k] in the chain
                ans += dp(k+1, i+1) * count[ord(c)][k]
                # to not exceed value of mod
                ans %= MOD
                
            return ans
        
        # Starting at 0th column, and from 0th index of target string. 
        return dp(0, 0)
            
            
        