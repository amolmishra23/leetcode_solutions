class Solution:
    def maxArea(self, h: int, w: int, hcut: List[int], vcut: List[int]) -> int:
        hcut, vcut = [0]+sorted(hcut)+[h], [0]+sorted(vcut)+[w]
        l, b = 0,0
        for i,j in zip(hcut[:-1], hcut[1:]): print(i, j); l=max(l, j-i)
        for i,j in zip(vcut[:-1], vcut[1:]): print(i, j); b=max(b, j-i)
        return (l*b)%((10**9)+7)