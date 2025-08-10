class Solution:
    def reorderedPowerOf2(self, N):
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in range(30))