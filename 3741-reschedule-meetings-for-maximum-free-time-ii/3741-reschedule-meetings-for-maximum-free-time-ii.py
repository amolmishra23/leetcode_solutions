from typing import List

class Solution:
    def maxFreeTime(self, eventTime, startTime, endTime):
        gap = [startTime[0]]
        for i in range(1, len(startTime)):
            gap.append(startTime[i] - endTime[i - 1])
        gap.append(eventTime - endTime[-1])

        largestRight = [0] * len(gap)
        for i in range(len(gap) - 2, -1, -1):
            largestRight[i] = max(largestRight[i + 1], gap[i + 1])

        ans = 0
        largestLeft = 0
        for i in range(1, len(gap)):
            # what duration does the meeting take??
            curGap = endTime[i - 1] - startTime[i - 1]

            if curGap <= max(largestLeft, largestRight[i]):
                # moving meeting to the biggest gap on left/right
                ans = max(ans, gap[i - 1] + gap[i] + curGap)

            # if we move meeting to 1 corner in same gap
            ans = max(ans, gap[i - 1] + gap[i])

            # so far the largest left block available
            largestLeft = max(largestLeft, gap[i - 1])

        return ans
