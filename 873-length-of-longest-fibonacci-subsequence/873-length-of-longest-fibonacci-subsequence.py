class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        """
        We consider elements in pairs of 2 here, and keep doing the future updates
        """
        n = len(A)
        lookup = {}
        
        for i in range(len(A)):
            lookup[A[i]] = i
        
        longest = collections.defaultdict(lambda: 2)
        
        maxLength = 2
        
        for i in range(len(A)):
            a = A[i]
            for j in range(i + 1, len(A)):
                b = A[j]
                c = a + b
                if c in lookup:
                    longest[(j, lookup[c])] = longest[(i, j)] + 1
                    maxLength = max(longest[(j, lookup[c])], maxLength)
        
        return maxLength if maxLength != 2 else 0