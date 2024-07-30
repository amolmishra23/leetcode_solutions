class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix_a = [0] * (n + 1)
        prefix_b = [0] * (n + 1)
        
        # Fill prefix arrays
        for i in range(n):
            prefix_a[i + 1] = prefix_a[i] + (s[i] == 'a')
            prefix_b[i + 1] = prefix_b[i] + (s[i] == 'b')
        
        res = float('inf')
        
        # Compute minimum deletions
        for i in range(n + 1):
            b_before = prefix_b[i]    # b's before position i
            a_after = prefix_a[n] - prefix_a[i]  # a's after position i
            res = min(res, b_before + a_after)
        
        return res