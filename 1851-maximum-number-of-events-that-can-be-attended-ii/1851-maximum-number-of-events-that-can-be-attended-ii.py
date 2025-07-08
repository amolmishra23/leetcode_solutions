class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x: x[0])
        n, memo = len(events), {}

        start_times = [e[0] for e in events]

        def dp(i, rem):
            if i==n or rem==0: return 0
            if (i,rem) in memo: return memo[(i, rem)]

            skip = dp(i+1, rem)
            
            next_index = bisect.bisect_left(start_times, events[i][1]+1)
            take = dp(next_index, rem-1) + events[i][2]

            memo[(i, rem)] = max(skip, take)
            
            return memo[(i, rem)]

        return dp(0,k)