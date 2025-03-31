class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1: return 0
        splits = sorted([weights[i] + weights[i+1] for i in range(len(weights)-1)])
        maxScore, minScore = sum(splits[-(k-1):]), sum(splits[:(k-1)])
        return maxScore-minScore