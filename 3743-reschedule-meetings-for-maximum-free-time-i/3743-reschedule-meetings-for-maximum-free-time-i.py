class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        gaps = []
        gaps.append(startTime[0]-0)
        for i in range(1, n):
            gaps.append(startTime[i]-endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        window_sum = sum(gaps[:k+1])
        max_free = window_sum

        for i in range(k+1, len(gaps)):
            window_sum += gaps[i] - gaps[i-(k+1)]
            max_free = max(window_sum, max_free)

        return max_free