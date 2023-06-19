class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heights = [0]
        for g in gain: heights.append(heights[-1]+g)
        return max(heights)