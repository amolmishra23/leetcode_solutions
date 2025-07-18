class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3

        # Step 1: Build prefix sums using max-heap
        maxHeap = []
        prefix = [0] * n
        sum_ = 0

        # process starting k element
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])  # use negation for max heap
            sum_ += nums[i]
        prefix[k - 1] = sum_

        # process more element and choose k only
        for i in range(k, 2 * k):
            if -maxHeap[0] > nums[i]:
                sum_ = prefix[i - 1] - (-heapq.heappop(maxHeap)) + nums[i]
                heapq.heappush(maxHeap, -nums[i])
                prefix[i] = sum_
            else:
                prefix[i] = prefix[i - 1]  # carry forward the previous sum

        # Step 2: Build suffix sums using min-heap
        minHeap = []
        suffix = [0] * n
        sum_ = 0

        for i in range(n - 1, n - k - 1, -1):
            heapq.heappush(minHeap, nums[i])
            sum_ += nums[i]
        suffix[n - k] = sum_

        for i in range(n - k - 1, k - 1, -1):
            if minHeap[0] < nums[i]:
                sum_ = suffix[i + 1] - heapq.heappop(minHeap) + nums[i]
                heapq.heappush(minHeap, nums[i])
                suffix[i] = sum_
            else:
                suffix[i] = suffix[i + 1]  # carry forward the previous sum

        # Step 3: Compute minimum difference of partitions
        ans = float('inf')
        for i in range(k - 1, 2 * k):
            ans = min(ans, prefix[i] - suffix[i + 1])

        return ans