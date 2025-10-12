class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        # Constants
        MOD = 10**9 + 7
        MAX_BIT = 60  # Sufficient to propagate all carries (max S ~ 30 * 2^49 < 2^55)
        n = len(nums)
        
        # Precompute factorial and inverse factorial for multinomial coefficients
        # fact[i] = i!
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # invfact[i] = (i!)^{-1} mod MOD (using Fermat's Little Theorem via pow)
        invfact = [0] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)  # Modular inverse of m!
        for i in range(m - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD  # invfact[i] = invfact[i+1] * (i+1)
        
        # DP setup: dp[i][j][c] = sum of [product over lower bits q: (nums[q]^{f[q]} * invfact[f[q]]) ] 
        # for configurations with 'i' items chosen, 'j' set bits from bits 0..(current-1), carry 'c' to current bit
        # Dimensions: i=0..m, j=0..k, c=0..m (carry <= m)
        prev = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(m + 1)]
        prev[0][0][0] = 1  # Base: before bit 0, 0 chosen, 0 bits, 0 carry
        
        # Process each bit position b from 0 to MAX_BIT-1
        for b in range(MAX_BIT):
            # Current layer for next bit
            curr = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(m + 1)]
            
            for i in range(m + 1):  # Items chosen so far
                for jj in range(k + 1):  # Set bits so far
                    for cc in range(m + 1):  # Incoming carry
                        val = prev[i][jj][cc]
                        if val == 0:
                            continue  # Skip empty states
                        
                        if b < n:  # Can choose f times the index b (exponent b)
                            max_f = m - i  # Can't exceed remaining items
                            for f in range(max_f + 1):  # Try f=0 to max_f
                                total = f + cc  # Total at this bit: choices + incoming carry
                                set_bit = total % 2  # Contributes to popcount if odd
                                new_c = total // 2  # Carry out to next bit
                                new_j = jj + set_bit
                                if new_j > k:
                                    continue  # Early prune: can't reach exactly k
                                
                                new_i = i + f  # New items chosen
                                # Update value: multiply by (nums[b]^f * invfact[f])
                                contrib = pow(nums[b], f, MOD) * invfact[f] % MOD * val % MOD
                                curr[new_i][new_j][new_c] = (curr[new_i][new_j][new_c] + contrib) % MOD
                        else:  # b >= n: no index, f=0, just propagate carry
                            total = cc
                            set_bit = total % 2
                            new_c = total // 2
                            new_j = jj + set_bit
                            if new_j > k:
                                continue
                            new_i = i
                            contrib = val  # No additional factor
                            curr[new_i][new_j][new_c] = (curr[new_i][new_j][new_c] + contrib) % MOD
            
            prev = curr  # Swap layers
        
        # Final answer: at highest bit, sum states with exactly m items, k bits, 0 carry * m!
        # (The * fact[m] completes the multinomial: m! * product (nums^f / f! over all) )
        ans = prev[m][k][0] * fact[m] % MOD
        return ans        