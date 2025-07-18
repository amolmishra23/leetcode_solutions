class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n, k = len(nums), len(nums)//3

        maxHeap, prefix, sum_ = [], [0]*n, 0

        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            sum_ += nums[i]
        prefix[k-1] = sum_

        for i in range(k, 2*k):
            if -maxHeap[0]>nums[i]:
                sum_ = prefix[i-1] - (-heapq.heappop(maxHeap)) + nums[i]
                heapq.heappush(maxHeap, -nums[i])
                prefix[i] = sum_
            else:
                prefix[i] = prefix[i-1]

        minHeap, suffix, sum_ = [], [0]*n, 0

        for i in range(n-1, n-k-1, -1):
            heapq.heappush(minHeap, nums[i])
            sum_ += nums[i]
        suffix[n-k] = sum_

        for i in range(n-k-1, k-1, -1):
            if minHeap[0]<nums[i]:
                sum_ = suffix[i+1] - heapq.heappop(minHeap) + nums[i]
                heapq.heappush(minHeap, nums[i])
                suffix[i] = sum_
            else:
                suffix[i] = suffix[i+1]

        res = float("inf")
        for i in range(k-1, 2*k):
            res = min(res, prefix[i] - suffix[i+1])

        return res