class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTime = [jobs[i][0] for i in range(n)]

        @lru_cache(None)
        def dp(i):
            if i == n: return 0
            # not doing the job
            ans = dp(i + 1)  # Choice 1: Don't pick

            # doing this job, and finding the next best job to do
            # after the current job ends at job[i][1], we need to find next best start time.
            j = bisect_left(startTime, jobs[i][1])
            
            # now adding profit of the current task, and doing it again from dp(j)
            # whose start doesnt collide with our end
            ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
            return ans

        return dp(0)